#from models import *
import sys
print(sys.path)
#from project import api
#from crew_api import project
#from . import api

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
