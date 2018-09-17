import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


## Initialize flask app and setup database connections
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database/data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## Initialize the SQLalchemy database
db = SQLAlchemy(app)
Migrate(app,db)

## Load flask blueprints
from featurerequest.features.views import feature_bp
app.register_blueprint(feature_bp)
