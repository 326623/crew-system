from flask import Blueprint
from flask_restplus import Api

#from crew_api.API.apis.user import api as user_api
from .apis.user import api as user_api
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

#api = Api(blueprint)

api = Api(app=blueprint,
    title='Rowing Crew API',
    version='1.0',
    description='First trial',
)

api.add_namespace(user_api)
