import logging
from flask import Flask, jsonify
from markupsafe import escape
# from flask_restful import Resource, Api
import json
from json import dumps

from databaseUtil import Util

app = Flask(__name__)
utilObj = Util()

@app.route('/')
def app_status():
    return 'App is working fine'


@app.route('/hello', methods=['GET'])
def say_hello():
    return 'Hello'


@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/users', methods=['GET'])
def show_users():
    users = None
    try:
        logging.info(f"before calling users")
        users = utilObj.getUsers()
        logging.info(f"after calling users")
    except Exception as e:
        logging.error(e)
        status = 'error'
        message = 'Error connecting to database'
        dictToReturn = {'status': status, 'message': message}
        return jsonify(dictToReturn)
    else:
        status = 'success'
        message = 'Connection to database established successfully'
        dictToReturn = {'status': status, 'message': message, 'users': users}
        return jsonify(dictToReturn)


@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


