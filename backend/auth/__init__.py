from flask import Blueprint, Flask, jsonify, redirect, session, url_for, request

#import cognito libraries
from flask_cognito_lib import CognitoAuth
from flask_cognito_lib.decorators import (
    auth_required,
    cognito_login,
    cognito_login_callback,
    cognito_logout,
)

app = Flask(__name__)
app.secret_key = "SecretKEY"

# Configuration required for CognitoAuth
app.config["AWS_REGION"] = "us-east-2"
app.config["AWS_COGNITO_USER_POOL_ID"] = "us-east-2_bXRj7cAEc"
app.config["AWS_COGNITO_DOMAIN"] = "https://testprof.auth.us-east-2.amazoncognito.com"
app.config["AWS_COGNITO_USER_POOL_CLIENT_ID"] = "1b94g6m6vmi9pmon9ictjamevq"
app.config["AWS_COGNITO_USER_POOL_CLIENT_SECRET"] = "3i2h87fqeiouodoac2l3dvhug8d7eommv35vatujgjvr3p79q99"
app.config["AWS_COGNITO_REDIRECT_URL"] = "http://localhost:5000/postlogin"
app.config["AWS_COGNITO_LOGOUT_URL"] = "http://localhost:5000/postlogout"

#import api files
from backend.auth.auth import *

#initialize app
app = Flask(__name__)

def build_auth():
        
    auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
    app.register_blueprint(auth_bp)

    return app
