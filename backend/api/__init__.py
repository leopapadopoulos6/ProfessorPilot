##########################################
# External Modules
##########################################

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from api import exception_views
from api.reviews import course_reviews_views
from api.security.auth0_service import auth0_service

from common.utils import safe_get_env_var

from .utils import CustomJSONEncoder

def create_app():
    ##########################################
    # Environment Variables
    ##########################################
    client_origin_url = safe_get_env_var("CLIENT_ORIGIN_URL")
    auth0_audience = safe_get_env_var("AUTH0_AUDIENCE")
    auth0_domain = safe_get_env_var("AUTH0_DOMAIN")

    ##########################################
    # Flask App Instance
    ##########################################

    app = Flask(__name__, instance_relative_config=True)
    app.json_encoder = CustomJSONEncoder #for mongodb
    

    ##########################################
    # HTTP Security Headers
    ##########################################

    csp = {
        'default-src': ['\'self\''],
        'frame-ancestors': ['\'none\'']
    }

    Talisman(
        app,
        force_https=False,
        frame_options='DENY',
        content_security_policy=csp,
        referrer_policy='no-referrer',
        x_xss_protection=False,
        x_content_type_options=True
    )

    auth0_service.initialize(auth0_domain, auth0_audience)

    @app.after_request
    def add_headers(response):
        response.headers['X-XSS-Protection'] = '0'
        response.headers['Cache-Control'] = 'no-store, max-age=0, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response

    ##########################################
    # CORS
    ##########################################

    CORS(
        app,
        resources={r"/api/*": {"origins": client_origin_url}},
        allow_headers=["Authorization", "Content-Type"],
        methods=["GET", "POST", "OPTIONS"],
        max_age=86400
    )

    # def add_cors_headers(response):
    #     response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
    #     response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    #     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    #     return response

    # app.after_request(add_cors_headers)
    ##########################################
    # Blueprint Registration
    ##########################################

    app.register_blueprint(course_reviews_views.bp)
    app.register_blueprint(exception_views.bp)

    return app
