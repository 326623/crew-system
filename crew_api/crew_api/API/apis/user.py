from flask_restplus import Namespace, Resource, fields
from crew_api import db
from crew_api.models import User

api = Namespace('user', description='user related operation')

# encrypt in front end
user_info = api.model('User', {
    'username': fields.String,
    'ID': fields.Integer,
    'email': fields.String
})

# @api.doc(params={'feature': 'the content of feture',
#                  'type': 'the type of feature'})
@api.doc(params={'id': 'id number'})
class user_api(Resource):
    @api.marshal_with(user_info)
    def get(self, id):
        user=None
        # would raise exception when multiple row is found or no row is found
        try:
            user=db.session.query(User).filter(User.ID == id).one()
        except:
            """operation for not found or multiple row is found"""
            pass
        return user

    #def post(self, ):


api.add_resource(user_api, '/<int:id>')
