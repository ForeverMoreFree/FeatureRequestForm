// Active view model.
function AppViewModel() {

	self = this;
	self.initialized = false // For one-time setup variables
	self.idCounter=0; // Used for client side in-memory database when not connected to database
	self.pages = ['Information', 'View Features', 'Add Feature']; //Update is hidden until called

	// KnockoutJS obserbables
	self.clients = ko.observable();
	self.productAreas = ko.observable();
	self.featureList = ko.observable();
	self.selectedPage = ko.observable();
	self.chosenClientId = ko.observable();
	self.chosenClientData = ko.observable();
	self.chosenFeatureData = ko.observable();
	self.formID = ko.observable();
	self.formTitle = ko.observable();
	self.formDesciption = ko.observable();
	self.formClient = ko.observable();
	self.formClientPriority = ko.observable();
	self.formTargetDate = ko.observable();
	self.formProductArea = ko.observable();
	self.responseJSON = ko.observable();
	self.enableDBConnection = ko.observable();
	self.dbStyleToggle = ko.observable();

	/** Navigation */
	// Change page focus
	self.selectPage = function(selection) {
		self.clearForm();
		self.chosenClientData(self.featureList()[self.chosenClientId()]);
		self.selectedPage(selection);
	};

	// Go to update page. Page hidden while deselected
	self.selectUpdatePage = function(data) { 
		self.populateFormData(data);
		self.selectedPage('Update Feature');
	};
	
	// Switch client view
    self.selectClient = function(client) {
		self.chosenClientId(client);
		self.chosenClientData(self.featureList()[self.chosenClientId()]);
	};


	/** CRUD - client and server */
	// Update feature
	self.updateLocalDB = function() {
		self.featureList(self.updateClientDB(self.featureList()));
	};

	// Delete feature (from update form)
	self.deleteFeatureButton = function() {
		if (self.enableDBConnection()){self.sendToAPI('DELETE',self.chosenFeatureData());}
		self.removeFeature();
		self.updateLocalDB();
		self.selectPage('View Features');
	};

  // Delete feature (from view features)
	self.removeFeatureButton = function(data) {
		self.populateFormData(data);
		if (self.enableDBConnection()){self.sendToAPI('DELETE',self.chosenFeatureData());}
		self.removeFeature();
		self.clearForm();
		self.updateLocalDB();
		self.selectPage('View Features');
	};

	// Remove feature logic
	self.removeFeature = function() {
		const index = self.featureList()[self.chosenClientId()].map(e =>
			e.id).indexOf(self.formID());
		if (index > - 1) {
			self.featureList()[self.chosenClientId()].splice(index, 1);
		}  
	};

	/** Form controls and logic */
  	// Clear form contents
	self.clearForm = function() {
		self.chosenFeatureData("");
		self.formID("");
		self.formTitle("");
		self.formDesciption("");
		self.formClient("");
		self.formClientPriority("");
		self.formTargetDate("");
		self.formProductArea("");
	};

	// Cancel form and return to 'View Features'
	self.cancelFeatureButton = function() {
		self.selectPage('View Features');
	};

	// Fill form data 
	self.populateFormData = function(data) {
		self.chosenFeatureData(data);
		self.formID(data.id);
		self.formTitle(data.title);
		self.formDesciption(data.description);
		self.formClient(self.chosenClientId());
		self.formClientPriority(data.clientPriority);
		self.formTargetDate(data.targetDate);
		self.formProductArea(data.productArea);
	};

	// Save form data. Send to api and local db. If api db connected, update client db.
	self.saveFormData = function() {
		if (Number.isInteger(Number(self.formClientPriority())) && Number(self.formClientPriority())>0) {
			self.formClientPriority(parseInt(self.formClientPriority()))
			if (self.formID() == "") {
				self.formID(self.idCounter);
				self.idCounter = self.idCounter + 1;
			}  
			else {
				self.removeFeature();
			}
			var tempVar = {
				"id" : self.formID(),
				"title" : self.formTitle(),
				"description" : self.formDesciption(),
				"client" : self.formClient(),
				"clientPriority" : self.formClientPriority(),
				"targetDate": self.formTargetDate(),
				"productArea" : self.formProductArea()
			};
			self.chosenFeatureData(tempVar);
			self.featureList()[self.formClient()].push(self.chosenFeatureData());
			if (self.enableDBConnection()){self.sendToAPI('CREATE',self.chosenFeatureData());}
			self.updateLocalDB();
			self.selectPage('View Features');


		}
		else {
			self.formClientPriority("")
		}
	};

	/** API logic */
	// Send command and data to api
	self.sendToAPI = function(action, data) {
		var toAPI = {
			'action': action,
			'data':data
		}
		self.getData(toAPI)
	};

	//Connect to database
	self.connectToDBToggle = function() {
		self.enableDBConnection(!self.enableDBConnection())
		if (self.enableDBConnection()){
			if (self.enableDBConnection()){self.sendToAPI('REQUEST',"")
			if (self.selectedPage() == "Add Feature" || self.selectedPage() == "Update Feature"){
				self.selectPage('View Features');
				}
			}

		}
	}

	self.dbStyleToggle = ko.pureComputed(function() {
        return self.enableDBConnection() > 0 ? "dbToggleOn" : "dbToggleOff";
    },self);

	// Takes responseFeatures type data and sorts it to be useable 
	self.filterResponse = function(responseFeatures) {
		var sortedFeatures = responseFeatures.sort(function(obj1, obj2) {
			return obj1.clientPriority - obj2.clientPriority;
		});
		var filtered = {}
		for (client in self.clients()) {
			filtered[self.clients()[client]] = [];
		}	
		for (var i = 0; i < sortedFeatures.length; i++) {
			for (var j = 0; j < self.clients().length; j++) {
				if (sortedFeatures[i]['client'] == self.clients()[j]) {
					filtered[self.clients()[j]].push(sortedFeatures[i]);
				}
			}
		}
		return filtered;
	};

	// Updates local in-memory db when not connected to DB 
	self.updateClientDB = function(localBDtoUpdate) {
		var tempList = [];
		for (key in localBDtoUpdate) {
			tempList.push(...localBDtoUpdate[key]);
		}
		return self.filterResponse(tempList);
	};

	// Top level API call. Recieves JSON data.
	self.getData = function(toAPI) {
		$.getJSON('/background_process',JSON.stringify(toAPI), function(data) {
			self.processResponse(data);
		})
		.error(function() {
			if (self.enableDBConnection()){self.connectToDBToggle() }
			 alert("Connection to database is not working. Try again later."); 
			})

	};

	// Process response data update bindings
	self.processResponse = function(data){
		self.responseJSON(data.response)
		if (self.responseJSON()['responseCode'] == 200){
			self.clients(self.responseJSON()["responseClients"]);
			self.productAreas(self.responseJSON()["responseProductArea"]);
			self.featureList(self.filterResponse(self.responseJSON()['responseFeatures']));
			self.idCounter = Number(self.responseJSON()['highestIDNumber'])+1
			self.chosenClientData(self.featureList()[self.chosenClientId()]);

			// If fist time connecting to db, use these bindings
			if (!self.initialized){
				self.initialized=true
				self.selectClient(self.responseJSON()['responseClients'][0]);
				self.selectPage(self.pages[0]);
			}
		}
		else{
			console.log("Reponse code: ", self.responseJSON()['responseCode'])
			console.log("Reponse message: ", self.responseJSON()['responseMessage'])
		}
	}

	// Get initial data
	self.enableDBConnection(false)
	self.connectToDBToggle() //Connect to database
	
};

// Activates knockout.js
document.addEventListener('DOMContentLoaded', () => {
ko.applyBindings(new AppViewModel());
});
