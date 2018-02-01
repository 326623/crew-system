
from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy


##########################
### Initialize the app ###
##########################



app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
api = Api(app)

from models import *


todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

