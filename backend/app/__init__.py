from flask import Flask, Blueprint

#import api files
from app.auth import *
from app.api import *
# from app.db import get_db #needs to be made

#initialize app
app = Flask(__name__)



# def build_api():
#     app.config.from_mapping(
#         SECRET_KEY='mysecretkey',
#         DATABASE_URL='dynamodb://localhost/myapp' #insert actual url
#     )

#     # Initialize the database connection
#     with app.app_context():
#         db = get_db()
#         db.init_app(app)

        
#     api_bp = Blueprint('api', __name__, url_prefix='/api')
#     app.register_blueprint(api_bp)

#     return app

def build_api():
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app