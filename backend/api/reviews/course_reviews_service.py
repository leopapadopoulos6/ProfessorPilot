from api.reviews.message import Message
from api import config
import uuid
import time
from flask import jsonify, request
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client_url = os.getenv('CLIENT')


client = MongoClient(client_url)
db = client['CourseReviews']
course_reviews = db['CourseReviews']

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


def submit_review():
    data = request.get_json()
    reviewer = data['reviewer']
    review_id = str(uuid.uuid4())
    timestamp = str(int(time.time() * 1000))

    course_review = {
        'PK': f'REVIEW#{review_id}',
        'SK': f'USER#{reviewer}',
        'GSI1PK': f'USER#{reviewer}',
        'CourseCode': data['course_code'],
        'CourseName': data['course_name'],
        'Difficulty': data['difficulty'],
        'Interest': data['interest'],
        'Usefulness': data['usefulness'],
        'Organization': data['organization'],
        'Workload': data['workload'],
        'Rating': data['rating'],
        'ReviewText': data['review_text'],
        'Term': data['term'],
        'Year': data['year'],
        'Upvotes': 0,
        'Status': 'active',
        'CreateDate': timestamp,
        'ModifiedDate': timestamp,
        'ReviewId': review_id
    }

    response = course_reviews.insert_one(course_review)
    return {"Message": "Submit Review Success"}


def get_recent_reviews():
    cursor = course_reviews.find({"PK": {"$regex": "^REVIEW#"}}).sort("CreateDate", -1).limit(25)
    recent_reviews = [{**review, '_id': str(review['_id'])} for review in cursor]
    return recent_reviews