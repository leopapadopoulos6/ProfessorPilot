from flask import Flask

#import api files
from backend.api.api import *
from backend.api.db import get_db #needs to be made

#initialize app
app = Flask(__name__)

def build_api():
    app.config.from_mapping(
        SECRET_KEY='mysecretkey',
        DATABASE_URL='dynamodb://localhost/myapp'
    )

    # Initialize the database connection
    with app.app_context():
        db = get_db()
        db.init_app(app)

        
    api_bp = Blueprint('api', __name__, url_prefix='/api')
    app.register_blueprint(api_bp)

    return app
