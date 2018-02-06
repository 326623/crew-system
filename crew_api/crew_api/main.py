##############
### import ###
##############

from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restplus import fields, Resource, Api
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig
from crew_api.models import Base, User
import os

##########################
### Initialize the app ###
##########################

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
db.Models = Base
#print(Base.metadata.tables)
#print(db.metadata.tables)
api = Api(app)
