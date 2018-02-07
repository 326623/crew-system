from .main import *
from .models import *
from .API.apiv1 import blueprint as api1
app.register_blueprint(api1)

if __name__ == '__main__':
    app.run(debug=True)
