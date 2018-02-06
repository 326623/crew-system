from flask_restplus import Namespace, Resource, fields
from crew_api.models import db, User

api = Namespace('user', description='user related operation')

# encrypt in front end
user_info = api.model('User', {
    'username': fields.String,
    'ID': fields.Integer,
    'email': fields.String
})

@api.route('/user/<int:id>')
@api.doc(params={'id': 'ID number'})
class user_api(Resource):
    @api.marshal_with(user_info)
    def get(self, id):
        # would raise exception when multiple row is found or no row is found
        user=db.query(User).filter(User.ID == id).one()
        print(user)
        return {'please': 'login'}


#api.add_resource(user_api, '/user/<int:id>')
