## This api is designed to act as a gatekeeper for database modifications.
## This makes it easy to update either side of the database connections.

## The project requirements explicitly say to:
    ## 'use "Client A", "Client B", "Client C" ' and
    ## "use 'Policies', 'Billing', 'Claims', 'Reports'"
## This can easily be done with one table. clientList and ProductList are dynamic and may be modified.

from main import db
#
# #Product areas and client List. May by modified.
clientList = ['Client A', 'Client B', 'Client C']
productAreaList = ['Policies', 'Billing', 'Claims', 'Reports']

## Our database's table model
class Feature(db.Model):
    __tablename__ = 'features'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    client = db.Column(db.Text)
    clientPriority = db.Column(db.Integer)
    targetDate = db.Column(db.Text)
    productArea = db.Column(db.Text)

    def __init__(self,title,description,client,clientPriority,targetDate,productArea):
        self.title = title
        self.description = description
        self.client = client
        self.clientPriority = clientPriority
        self.targetDate = targetDate
        self.productArea = productArea


## Create new Feature in table
def createFeature(data):
    try:
        updatePriorities(data)
    except:
        return 100, "Could not reorder features try again."
    try:
        new_feature = Feature(data['title'],
                              data['description'],
                              data['client'],
                              data['clientPriority'],
                              data['targetDate'],
                              data['productArea'])
        db.session.add(new_feature)
        db.session.commit()
        return 200, ''
    except:
        return 100, 'Could not create feature, please try again.'


## Update a single feature
def updateFeature(data):
    responseCode = 200
    responseMessage= ''
    try:
        try:
            responseCode, responseMessage = updatePriorities(data)
        except:
            return 100, "Could not reorder features try again."

        if responseCode == 200:
            feature = Feature.query.filter_by(id=data['id']).first()
            feature.title = data['title']
            feature.description = data['description']
            feature.client = data['client']
            feature.clientPriority = data['clientPriority']
            feature.targetDate = data['targetDate']
            feature.productArea = data['productArea']
            db.session.commit()
            return 200, ''
        else:
            return responseCode, responseMessage
    except Exception as e:
        # print('Somthing went wrong')
        return 999,"Could not update feature. Error code: " + str(e)

## Delete a feature
def deleteFeature(data):
    try:
        if db.session.query(Feature.query.filter(Feature.id == data['id']).exists()).scalar():
            feature_to_del = queryGetFeature(data['id'])
            db.session.delete(feature_to_del)
            db.session.commit()
            return 200, ''
        else:
            return 100, "User does not exist"
    except:
        return 100, "Delete failed. Try again."

## Return list of features
def queryAllDict():
    featureList=[]
    allFeatures=Feature.query.all()
    for row in allFeatures:
        tempDict = {}
        for column in row.__table__.columns:
            tempDict[column.name] = str(getattr(row, column.name))
        featureList.append(tempDict)
    return featureList

## Return highest id number in table
def highestIDNumber():
    maxid=[]
    allFeatures=Feature.query.all()
    for row in allFeatures:
        for column in row.__table__.columns:
            if column.name == 'id':
                maxid.append(int(str(getattr(row, column.name))))

    return max(maxid)

## Return Feature
def queryGetFeature(id):
    return Feature.query.get(id)


## Update priorities based on incoming action and priority.
## Does not change priorities if deleting. This is intentional.
def updatePriorities(data):
    try:
        featureList = queryAllDict()
        features = [d for d in featureList if d['client'] == data['client'] if int(d['clientPriority']) >= int(data['clientPriority']) and not data['id'] == d['id']]
        features = sorted(features, key=lambda i: int(i['clientPriority']))
        for x in range(len(features)):
            if not int(features[0]['clientPriority']) == int(data['clientPriority']):
                break
            singleFeature = Feature.query.get((features[x]['id']))
            singleFeature.clientPriority += 1
            if x == len(features) - 1 or not int(features[x]['clientPriority']) + 1 == int(
                    features[x + 1]['clientPriority']):
                break
        db.session.commit()
        return 200, ''

    except Exception as e:
        print('Somthing went wrong in updatePriorities')
        return 999, str(e)


## Validates incoming form data. Responds with appropriate error codes if a field validation fails.
def validateFeature(data):
    formErrors = []
    try:
        int(data['id'])
    except:
        formErrors.append('id must be an integer greater than zero.')
    if not isinstance(data['title'], str): formErrors.append('The title must be text.')
    if not isinstance(data['description'], str): formErrors.append('The description must be text.')
    if not data['client'] in clientList: formErrors.append('Client does not exist.')
    try:
        int(data['clientPriority'])
    except:
        formErrors.append('Priority must be an integer greater than zero.')
    if not isinstance(data['targetDate'], str): formErrors.append('The target date must be text.')
    if not data['productArea'] in productAreaList: formErrors.append('Product area does not exist.')
    if not len(formErrors):
        return 200, ''
    else:
        return 100, f'You have the follow errors: {" ".join(formErrors)}'
