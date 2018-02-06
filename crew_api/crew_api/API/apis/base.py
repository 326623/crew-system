from flask_restplus import Namespace, Resource, fields

api = Namespace('')

class login(Resource):
    def get(self):
        return {'please': 'login'}

