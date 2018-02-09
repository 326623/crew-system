# from .main import *
# from .models import *
# from .API.apiv1 import blueprint as api1
# app.register_blueprint(api1)

# #__all__ = ['app']

# if __name__ == '__main__':
#     app.run(debug=True)

##############
### import ###
##############

from flask import Flask, request
from flask_bcrypt import Bcrypt
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
bcrypt = Bcrypt(app)

##########################
### import app command ###
##########################

import crew_api.command

from crew_api.API.apiv1 import blueprint as api1
app.register_blueprint(api1)
