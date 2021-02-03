import logging
from flask import Flask, jsonify, Response
from markupsafe import escape
from flask_api import FlaskAPI, status
# from flask_restful import Resource, Api
import json
from json import dumps

from databaseUtil import Util

app = FlaskAPI(__name__)
utilObj = Util()

@app.route('/')
def app_status():
    return 'App is working fine', status.HTTP_200_OK


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
        users = utilObj.getUsers()
    except Exception as e:
        logging.error(e)
        message = 'Error connecting to database'
        dictToReturn = { 'message': message}
        return jsonify(dictToReturn), status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'success'
        dictToReturn = {'message': message, 'users': users}
        return jsonify(dictToReturn), status.HTTP_200_OK


@app.route('/users/<int:user_id>', methods=['GET'])
def show_user_by_id(user_id):
    try:
        user = utilObj.getUserById(user_id)
    except Exception as e:
        logging.error(e)
        message = 'Error connecting to database'
        dictToReturn = { 'message': message}
        return jsonify(dictToReturn), status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = 'success'
        dictToReturn = {'message': message, 'user': user}
        return jsonify(dictToReturn), status.HTTP_200_OK

@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.run(debug=True)


