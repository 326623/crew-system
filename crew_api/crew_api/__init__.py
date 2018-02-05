##############
### config ###
##############

import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://crew-root:crew-root@localhost/crewmen'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    HASHING_METHOD = 'sha512'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test@localhost/test'


##############
### import ###
##############

from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restplus import fields, Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os

##########################
### Initialize the app ###
##########################

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
api = Api(app)
