import os, json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import url_for, redirect, request, jsonify

## Initialize flask app and setup database connections
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


## Initialize the SQLalchemy database
db = SQLAlchemy(app)
Migrate(app, db)
import api as db_api

## Creates "index" page
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return redirect(url_for('static', filename='index.html'))


## Shuttles information between frontend and backend.
@app.route('/background_process', methods=['GET', 'POST'])
def background_process():
    try:
        ## Default response information
        responseCode = 200
        responseMessage = ''

        ## Gather JSON data and parse
        incomingData = request.args.to_dict(flat=False)
        dataToParse = json.loads(list(incomingData)[0])
        action = dataToParse['action']
        data = dataToParse['data']

        ## If something is to be changed in the database, ask api to validate first
        if action == 'CREATE' or action == 'DELETE':
            responseCode, responseMessage = db_api.validateFeature(data)

        ## Perform desired action
        if responseCode == 200:
            if action == 'REQUEST': pass
            elif action == 'DELETE':
                try:
                    responseCode, responseMessage = db_api.deleteFeature(data)
                except:
                    responseCode = 100
                    responseMessage = 'Did not delete properly. Try again.'
            elif action == 'CREATE':
                if int(data['id']) > db_api.highestIDNumber():  # create
                    responseCode, responseMessage = db_api.createFeature(data)
                elif int(data['id']) >= 1:  # update
                    responseCode, responseMessage = db_api.updateFeature(data)
                else:
                    responseCode = 110
                    responseMessage = 'id must be an integer greater than zero.'
            else:
                responseCode = 98
                responseMessage = "Please send an action to perform"

            ## If action success, continue collecting response data
            if responseCode == 200:
                try:
                    ##Construct response
                    clientList = db_api.clientList
                    responseFeatures = db_api.queryAllDict()
                    productAreaList = db_api.productAreaList
                    highestIDNumber = db_api.highestIDNumber()
                    response = {
                        "responseCode": responseCode,
                        "responseMessage": responseMessage,
                        "responseClients": clientList,
                        "responseProductArea": productAreaList,
                        "responseFeatures": responseFeatures,
                        "highestIDNumber": highestIDNumber,
                    }
                    return jsonify(response=response)
                except:
                    responseCode = 100
                    responseMessage = "Error connecting to database or api. Try again."
        ## If anything fails send error code and error message
        response = {
            "responseCode": responseCode,
            "responseMessage": responseMessage,
        }
        return jsonify(response=response)

    except Exception as e:
        # print('Somthing went wrong')
        return str(e)

if __name__ == "__main__":
    amIInDockerContainer = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)
    if amIInDockerContainer:
        app.run(port=80, debug=False, host='0.0.0.0')
    else:
        app.run()
