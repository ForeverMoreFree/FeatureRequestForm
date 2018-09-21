/** Example GET and responses */
// Sample JSON response
var exampleJSON = {
	"responseCode":200,
	"responseMessage":'',
	"responseClients":['Client A', 'Client B', 'Client C'],
	"responseProductArea":['Policies', 'Billing', 'Claims','Reports'],
	"responseFeatures":[
		{
			"id": 1,
			"title": "Connect api beteween decoupled frontend/backend",
			"description": "I have already created the api, need to install on frontend and backend.",
			"client": "Client A",
			"clientPriority": "1",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 10,
			"title": "Add server-side database validation",
			"description": "Client-side form validations completed. Do the same for database api validations.",
			"client": "Client A",
			"clientPriority": "2",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 50,
			"title": "Add dynamic priority sorting on server-side",
			"description": "Create sorting mechanism for client priorities",
			"client": "Client A",
			"clientPriority": " 3",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 4,
			"title": "Update reponse codes and corresponding logic on clientside",
			"description": "create a list of appropriate response codes",
			"client": "Client A",
			"clientPriority": "4",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 12,
			"title": "Add client table and product area table. Api load on app.py start",
			"description": "Add client table and product area table. Api load on app.py start",
			"client": "Client A",
			"clientPriority": "5",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 11,
			"title": "Place app in docker container!",
			"description": "Dockerize!",
			"client": "Client A",
			"clientPriority": "10",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 7,
			"title": "Host app that is in docker container",
			"description": "Host app that is in docker container",
			"client": "Client A",
			"clientPriority": "17",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 8,
			"title": "General cleanup and submission",
			"description": "General cleanup and submission",
			"client": "Client A",
			"clientPriority": "30",
			"targetDate": "09/20/2018",
			"productArea": "Policies"
		},
		{
			"id": 5,
			"title": "Placeholder 2 Title",
			"description": "Placeholder 1 description",
			"client": "Client B",
			"clientPriority": "1",
			"targetDate": "01/01/2031",
			"productArea": "Policies"
		},
		{
			"id": 9,
			"title": "Placeholder 2 Title",
			"description": "Placeholder 2 description",
			"client": "Client B",
			"clientPriority": "2",
			"targetDate": "01/01/2032",
			"productArea": "Policies"
		},
		{
			"id": 6,
			"title": "Placeholder 1 Title",
			"description": "Placeholder 1 description",
			"client": "Client C",
			"clientPriority": "5",
			"targetDate": "06/06/2019",
			"productArea": "Policies"
		},
		{
			"id": 2,
			"title": "Placeholder 2 Title",
			"description": "Placeholder 2 description",
			"client": "Client C",
			"clientPriority": "8",
			"targetDate": "06/07/2019",
			"productArea": "Policies"
		},
		{
			"id": 41,
			"title": "Placeholder 3 description",
			"description": "Placeholder 2 description",
			"client": "Client C",
			"clientPriority": "23",
			"targetDate": "06/08/2019",
			"productArea": "Policies"
		}
	]

};

// Sample GET for the API



// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI
function AppViewModel() {

	self = this;
	self.idCounter=1000; // only used for pre-api use to add client users
	self.pages = ['Information', 'View Features', 'Add Feature']; //Update is hidden until called
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

	/** Navigation */
	// Change page focus
	self.selectPage = function(selection) {
		self.clearForm();
		self.chosenClientData(self.featureList()[self.chosenClientId()]);
		self.selectedPage(selection);
	};

	// Go to update page
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
		self.sendToAPI({'DELETE':self.chosenFeatureData()});
		self.removeFeature();
		self.updateLocalDB();
		self.selectPage('View Features');
	};

  // Delete feature (from view features)
	self.removeFeatureButton = function(data) {
		self.populateFormData(data);
		self.sendToAPI({'DELETE':self.chosenFeatureData()});
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

	// Cancel form and return to "Information"
	self.cancelFeatureButton = function() {
		self.selectPage('Information');
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

	// Save form data (add feature calls directly here,
	  	//update feature removes exisiting feature first )
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
			self.sendToAPI({'CREATE':self.chosenFeatureData()});
			self.updateLocalDB();
			self.selectPage('View Features');


		}
		else {
			self.formClientPriority("")
		}
	};

	/** API logic */
	// Send command and data to api
	self.sendToAPI = function(data) {
		// Send this data to api
	};

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

	self.updateClientDB = function(localBDtoUpdate) {
		var tempList = [];
		for (key in localBDtoUpdate) {
			tempList.push(...localBDtoUpdate[key]);
		}
		return self.filterResponse(tempList);
	};

	/** Default bindings */
	self.clients(exampleJSON["responseClients"]);
	self.productAreas(exampleJSON["responseProductArea"]);
	self.featureList(self.filterResponse(exampleJSON['responseFeatures']));
	self.selectClient(exampleJSON['responseClients'][0]);
	self.selectPage(self.pages[0]); 
	self.sendToAPI({'REQUEST':''});
 
};

// Activates knockout.js
document.addEventListener('DOMContentLoaded', () => {
ko.applyBindings(new AppViewModel());
});
