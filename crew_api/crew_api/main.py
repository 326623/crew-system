##############
### import ###
##############

from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restplus import fields, Resource, Api
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig
import os

##########################
### Initialize the app ###
##########################

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
api = Api(app)
