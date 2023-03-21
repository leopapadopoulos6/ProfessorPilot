from flask import Flask, jsonify, redirect, session, url_for, request, Blueprint

app = Flask(__name__)


#Home

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    log = {'John': 'Smith'}
    #return jsonify(log)
    return (log)

@app.route('/reviews', methods=['GET'])
def top_reviews():
    return 'Hi'


#Courses

@app.route('/reviews/courses', methods=['GET'])
def get_courses():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/reviews/courses/<course>', methods=['GET'])
def get_course():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/reviews/courses/<course>', methods=['POST'])
def post_course_review():
    log = {'x': 'y'}
    print(log)
    return log


#Professors

@app.route('/reviews/professors',  methods=['GET'])
def get_professors():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/reviews/professors/<professor>', methods=['GET'])
def get_professor():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/reviews/professors/<professor>', methods=['POST'])
def post_professor_review():
    log = {'x': 'y'}
    print(log)
    return log


#Discussions

@app.route('/discussions',  methods=['GET'])
def get_discussions():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/discussions',  methods=['POST'])
def post_discussion():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/discussions/<discussion>',  methods=['GET'])
def get_comments():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/discussions/<discussion>',  methods=['POST'])
def post_comment():
    log = {'x': 'y'}
    print(log)
    return log


#Misc.

@app.route('/contact', methods=['POST'])
def contact_us():
    log = {'x': 'y'}
    print(log)
    return log



