import logging
from flask import Flask, jsonify, request, Response
from flask_bcrypt import Bcrypt

from markupsafe import escape
from flask_api import FlaskAPI, status
# from flask_restful import Resource, Api
import json
from json import dumps
log_dir = 'var/logs/error.log'
logging.basicConfig(filename=log_dir,  format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

from databaseUtil import Util

app = FlaskAPI(__name__)
bcrypt = Bcrypt(app)
utilObj = Util()

@app.route('/')
def app_status():
    return 'App is working fine', status.HTTP_200_OK


@app.route('/hello', methods=['GET'])
def say_hello():
    return 'Hello world'

'''
@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

'''
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


@app.route('/users/<string:user_id>', methods=['GET'])
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

@app.route('/delUsers/<string:user_id>', methods=['GET'])
def remove_user_by_id(user_id):
    try:
        msg = utilObj.removeUserById(user_id)
    except Exception as e:
        logging.error(e)
        message = 'Error connecting to database'
        dictToReturn = { 'message': message}
        return jsonify(dictToReturn), status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = msg
        dictToReturn = {'message': message}
        return jsonify(dictToReturn), status.HTTP_200_OK

@app.route('/createUser', methods=['POST'])
def create_user():
    try:
        # logging.info(f'entered try block')
        # logging.debug(f'{request}')
        # username = str(request.data.get('username',''))
        # logging.info(f'username {username}')
        pw_hash = bcrypt.generate_password_hash(request.data.get('password')).decode('utf-8')
        msg = utilObj.insertUser(request.data.get('username'), request.data.get('name'),
                                 request.data.get('email'), pw_hash )
    except Exception as e:
        logging.error(e)
        message = 'Error connecting to database'
        dictToReturn = { 'message': message}
        return jsonify(dictToReturn), status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = msg
        dictToReturn = {'message': message}
        return jsonify(dictToReturn), status.HTTP_200_OK

@app.route('/updateUser', methods=['POST'])
def update_user():
    try:
        # logging.info(f'entered try block')
        # logging.debug(f'{request}')
        # username = str(request.data.get('username',''))
        # logging.info(f'username {username}')
        msg = utilObj.updateUser(request.data.get('username'), request.data.get('name'),
                                 request.data.get('email'), request.data.get('id'))
    except Exception as e:
        logging.error(e)
        message = 'Error connecting to database'
        dictToReturn = { 'message': message}
        return jsonify(dictToReturn), status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        message = msg
        dictToReturn = {'message': message}
        return jsonify(dictToReturn), status.HTTP_200_OK


@app.route('/login', methods=['POST'])
def login_user():
    try:
        username_entered = request.data.get('username')
        password_entered = request.data.get('password')
        db_hash = utilObj.login(username_entered)
        logging.info(f'db_hash -> {db_hash}')
    except Exception as e:
        logging.error(e)
        message = 'Error connecting to database'
        dictToReturn = { 'message': message}
        return jsonify(dictToReturn), status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        pw_hash = bcrypt.generate_password_hash(password_entered).decode('utf-8')
        logging.info(f'db_hash -> {db_hash} pw_hash -> {pw_hash}')
        if bcrypt.check_password_hash(db_hash, password_entered):
            message = 'success'
        else:
            message = 'password is not correct'
        dictToReturn = {'message': message}
        return jsonify(dictToReturn), status.HTTP_200_OK











'''

@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id



@app.route('/users', methods=['GET'])
def show_users():
    users = None
    dictToReturn = ({'name': 'john', 'age': 22},{'name': 'johny', 'age': 32})
    return jsonify(dictToReturn), status.HTTP_200_OK



@app.route('/users/<int:user_id>', methods=['GET'])
def show_user_by_id(user_id):
    dictToReturn = {'name': 'john', 'age': 22}
    return jsonify(dictToReturn), status.HTTP_200_OK

'''

if __name__ == "__main__":
    app.run(debug=True)


