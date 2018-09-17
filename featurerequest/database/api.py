## This api is designed to act as a gatekeeper for database modifications.
## This makes it easy to update either side of the database connections.

## The project requirements explicitly say to:
    ## 'use "Client A", "Client B", "Client C" ' and
    ## "use 'Policies', 'Billing', 'Claims', 'Reports'"
## This can easily be done with one database.

from sqlalchemy.sql import exists
from featurerequest import db
from featurerequest.database.model import Feature


## Create new Feature in database
def newFeature(title, description, client, client_priority, target_date, product_area):
    new_feature = Feature(title,
                          description,
                          client,
                          client_priority,
                          target_date,
                          product_area)
    db.session.add(new_feature)
    db.session.commit()
    # reorderPriorities() # This is a placeholder. Will be implemented later.


## To be implemented in a future version
## Update a single feature
def updateFeature():
    # reorderPriorities() # This is a placeholder. Will be implemented later.
    pass

## To be implemented in a future version
## Update priority list on database change
def reorderPriorities():
    pass


## Delete a feature
def deleteFeature(id):
    if db.session.query(Feature.query.filter(Feature.id == id).exists()).scalar():
        feature_to_del = queryGetID(id)
        db.session.delete(feature_to_del)
        db.session.commit()
        #reorderPriorities() # This is a placeholder. Will be implemented later.
        return 200
    else:
        return "User does not exist"


def queryAll():
    return Feature.query.all()


def queryGetID(id):
    return Feature.query.get(id)








