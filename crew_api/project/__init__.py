##############
### import ###
##############

from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restplus import fields, Resource, Api
from flask_sqlalchemy import SQLAlchemy


##########################
### Initialize the app ###
##########################

app = Flask(__name__)
#app.config.from_object('config.DevelopmentConfig')
app.config.from_object('config.TestConfig')
db = SQLAlchemy(app)
api = Api(app)

print (__name__)
