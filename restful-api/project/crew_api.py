
from flask import Flask, request
#from flask_restful import Resource, Api
from flask_restplus import fields, Resource, Api
from flask_sqlalchemy import SQLAlchemy


##########################
### Initialize the app ###
##########################



app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
api = Api(app)

from models import *

print (__name__)

todos = {}

# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}


# @api.route('/my-resource/<id>', endpoint='my-resource')
# @api.doc(params={'id': 'An ID'})
# class MyResource(Resource):
#     def get(self, id):
#         return {}

#     @api.doc(responses={403: 'Not Authorized'})
#     def post(self, id):
#         api.abort(403)


#api.add_resource(TodoSimple, '/<string:todo_id>')
#api.add_resource(MyResource)

from collections import OrderedDict

# from flask import Flask
# from flask_restplus import fields, Api, Resource

# app = Flask(__name__)
# api = Api(app)

model = api.model('Model', {
    'task': fields.String,
    'id': fields.Integer
#    'uri': fields.Url('todo_ep')
})

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

@api.route('/todo')
class Todo(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

if __name__ == '__main__':
    app.run(debug=True)
