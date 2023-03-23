from flask import Flask, request
from api import api
from api.messages.message import Message


from course_review import CourseReview



def get_public_message():
    return Message(
        "This is a public message."
    )

def get_protected_message():
    return Message(
        "This is a protected message."
    )

def get_admin_message():
    return Message(
        "This is an admin message."
    )

#Home
def submit_review(data):
    data = request.get_json()

    course_review = CourseReview()
    course_review.create_review(
    reviewer=data['reviewer'],
    coursename=data['course_name'],
    criteria=[data['difficulty'], data['interest'], data['usefulness'], data['organization'], data['workload'], data['rating']],
    code=data['course_code'],
    text=data['review_text'],
    term=data['term'],
    year=data['year']
)
    
    return jsonify({'message': 'Review submitted successfully'}), 201

def recent_reviews():
    return Message(
        "most recent reviews"
    )

def trending_courses():
    return Message(
        "Courses with recent reviews"
    )

# #Courses

# def get_courses():
#     return Message(
#         "list of all courses"
#     )


# def get_course_reviews():
#     return Message(
#         "list reviews for specific course"
#     )


# def post_course_review():
#     return Message(
#         "post a review for a course"
#     )

# #Professors

# def get_professors():
#     return Message(
#         "list of all professors"
#     )


# def get_professor_reviews():
#     return Message(
#         "list reviews for specific professor"
#     )


# def post_professor_review():
#     return Message(
#         "post a review for a professor"
#     )

# #Discussions

# def get_discussions():
#     return Message(
#         "list of all discussions"
#     )

# def post_discussion():
#     return Message(
#         "post a discussion"
#     )

# def get_discussion():
#     return Message(
#         "get a specific discussion post. View a full post with comments"
#     )

# def post_comment():
#     return Message(
#         "post a comment to a discussion"
#     )

# #Misc

# def post_contact():
#     return Message(
#         "post to contact us"
#     )