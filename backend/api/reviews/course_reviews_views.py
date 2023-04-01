import flask
from flask import (
    Flask, Blueprint, request, jsonify
)


from .course_reviews_service import (
    get_public_message,
    get_protected_message,
    get_admin_message,
    submit_course_review,
    get_recent_course_reviews,
<<<<<<< HEAD
    get_all_courses,
    get_reviews_by_course_code
    get_recent_course_reviews
=======
    get_all_course_reviews,
    get_course_reviews
>>>>>>> 3125e88 (added functions for reviews)
)
from ..security.guards import (
    authorization_guard,
    permissions_guard,
    admin_messages_permissions
)



bp_name = 'api-reviews'
bp_url_prefix = '/api/reviews'
bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix)

@bp.route('/', methods=(['GET', 'POST']))
@bp.route('/home', methods=(['GET', 'POST', 'OPTONS']))
@bp.route('/recent_course_reviews', methods=['GET', 'OPTIONS'])
#@authorization_guard

def home():
    if request.method == 'GET':
        recent_course_reviews = get_recent_course_reviews()  # Remove the arguments from the function call
        response = jsonify(recent_course_reviews)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        # const recentreviews = await response.json();
        # console.log('Recent review data:', recentreviews);
        return response, 200
    if request.method == 'OPTIONS':
        response = flask.Response(status=200)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response
   
@bp.route('/submit_course_review', methods=['GET', 'POST', 'OPTIONS'])
def submit_course_review():
     
    if request.method == 'POST':
        val = submit_course_review()
        return jsonify(val), 200
<<<<<<< HEAD

@bp.route("/recent_course_reviews", methods=["GET", "OPTIONS"])
def recent_entries():
    if request.method == 'GET':
        recent_course_reviews = get_recent_course_reviews()
        for entry in recent_course_reviews:
            entry["_id"] = str(entry["_id"])
        response = jsonify(recent_course_reviews)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response, 200
    if request.method == 'OPTIONS':
        response = flask.Response(status=200)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response

@bp.route('/courses/<courseCode>', methods=['GET', 'OPTIONS'])
def get_course_reviews(courseCode):  
    "Gets reviews for a specific course"
    if request.method == 'OPTIONS':
        response = flask.Response(status=200)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response
    if request.method == 'GET':
        course_reviews = get_reviews_by_course_code(courseCode)
=======
  

@bp.route('/all_course_reviews', methods=['GET', 'OPTIONS'])
def get_all_course_reviews():  
    "Gets all course reviews"
    if request.method == 'GET':
        course_reviews = get_all_course_reviews
>>>>>>> 3125e88 (added functions for reviews)
        response = jsonify(course_reviews)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'

        return response, 200
<<<<<<< HEAD



#COURSES
@bp.route('/courses', methods=(['GET', 'OPTIONS']))
@bp.route('/coursesPage', methods=(['GET', 'OPTIONS']))
def get_courses():
    if request.method == 'GET':
        courses = get_all_courses()
        response = jsonify(courses)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response, 200
    if request.method == 'OPTIONS':
        response = flask.Response(status=200)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response
    


@bp.route("/public")
def public():
    return vars(get_public_message())


@bp.route("/protected")
@authorization_guard
def protected():
    return vars(get_protected_message())


@bp.route("/admin")
@authorization_guard
@permissions_guard([admin_messages_permissions.read])
def admin():
    return vars(get_admin_message())


# @bp.route("/courses", methods=["GET"])
# def get_courses():
#     if request.method=='GET':
#         courses = get_all_courses()
#         response = jsonify(courses)
#         response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
#         response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
#         response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
#         return response, 200
=======
    
@bp.route('/courses/<course_name>/course_reviews', methods=['GET', 'OPTIONS'])
def get_course_reviews(course_name:str):  

    "Gets reviews for a specific course"
    if request.method == 'GET':
        course_reviews = get_course_reviews(course_name)
        response = jsonify(course_reviews)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:4040'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'

        return response, 200
>>>>>>> 3125e88 (added functions for reviews)
