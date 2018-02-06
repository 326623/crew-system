from API.apiv1 import blueprint as api1
from crew_api import app

app.register_blueprint(api1)

