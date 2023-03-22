from flask import (
    Blueprint
)

from api.messages.messages_service import (
    get_public_message,
    get_protected_message,
    get_admin_message, 
    recent_reviews,
    trending_courses,
    get_courses,
    get_course_reviews,
    post_course_review,
    get_professors,
    get_professor_reviews,
    post_professor_review,
    get_discussions,
    post_discussion,
    get_discussion,
    post_comment,
    post_contact

)
from api.security.guards import (
    authorization_guard,
    permissions_guard,
    admin_messages_permissions
)

bp_name = 'api-messages'
bp_url_prefix = '/api/messages'
bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix)


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
    return vars(get_admin_message(), trending_courses())


#Home

@bp.route('/', methods=['GET'])
@bp.route('/home', methods=['GET'])
def home():
    return (vars(recent_reviews))


#Courses

@bp.route('/reviews/courses', methods=['GET'])
def courses():

    return (vars(get_courses))

@bp.route('/reviews/courses/<course>', methods=['GET'])
def view_course_reviews():

    return (vars(get_course_reviews))

@bp.route('/reviews/courses/<course>', methods=['POST'])
def create_course_review():

    return post_course_review



#Professors

@bp.route('/reviews/professors',  methods=['GET'])
def professors():
    return (vars(get_professors))

@bp.route('/reviews/professors/<professor>', methods=['GET'])
def view_professor_reviews():
    return (vars(get_professor_reviews))

@bp.route('/reviews/professors/<professor>', methods=['POST'])
def create_professor_review():
    return (vars(post_professor_review))


#Discussions

@bp.route('/discussions',  methods=['GET'])
def view_discussions():
    return (vars(get_discussions))

@bp.route('/discussions',  methods=['POST'])
def create_discussion():
    return (vars(post_discussion))

@bp.route('/discussions/<discussion>',  methods=['GET'])
def view_discussion():
    return (vars(get_discussion))

@bp.route('/discussions/<discussion>',  methods=['POST'])
def create_comment():
    return (vars(post_comment))


#Misc.

@bp.route('/contact', methods=['POST'])
def contact_us():
    return post_contact



