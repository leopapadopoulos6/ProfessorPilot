from flask import Flask, jsonify, redirect, session, url_for, request, Blueprint

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    log = {'John': 'Smith'}
    #return jsonify(log)
    return (log)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/professors',  methods=['GET', 'POST'])
def professors():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/discussions',  methods=['GET', 'POST'])
def discussions():
    log = {'x': 'y'}
    print(log)
    return log

@app.route('/contact')
def contact():
    log = {'x': 'y'}
    print(log)
    return log
