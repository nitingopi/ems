import logging
import json


from config import config
configObj = config()


class Util:

    def __init__(self):
        self.cursor = configObj.get_cursor()

    def getUsers(self):
        try:
            logging.info(f"before query")
            query = "SELECT * FROM users"
            logging.info(f"query --> {query}")
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            # file_name = results['file_name']
        except Exception as e:
            logging.error(e)
            return e
        else:
            return results

    def getUserById(self, id):
        try:
            query = "SELECT username FROM users where user_id=%s "
            logging.info(f"query --> {query}")
            self.cursor.execute(query, id)
            results = self.cursor.fetchone()
            # file_name = results['file_name']
        except Exception as e:
            logging.error(e)
            return e
        else:
            return results

    def removeUserById(self, id):
        try:
            query = "DELETE FROM users where user_id=%s "
            logging.info(f"query --> {query}")
            self.cursor.execute(query, id)
            # results = self.cursor.fetchone()
            # file_name = results['file_name']
        except Exception as e:
            logging.error(e)
            return e
        else:
            return 'success'

    def insertUser(self, username, name, email, password, createdDate, updatedDate):
        try:
            query = "INSERT INTO users ( username, name, email, password, created_date, updated_date ) VALUES ( %s, %s, %s, %s, %s, %s )"
            logging.info(f"query --> {query}")
            self.cursor.execute(query, (username, name, email, password, createdDate, updatedDate))
            # results = self.cursor.fetchone()
            # file_name = results['file_name']
        except Exception as e:
            logging.error(e)
            return e
        else:
            return 'success'

    def updateUser(self, username, name, email, id, updated_date):
        try:
            query = "UPDATE users SET username = %s, name = %s , email = %s," \
                    " updated_date = %s WHERE user_id = %s "
            logging.info(f"query --> {query}")
            self.cursor.execute(query, (username, name, email, updated_date, id))
            # results = self.cursor.fetchone()
            # file_name = results['file_name']
        except Exception as e:
            logging.error(e)
            return e
        else:
            return 'success'

    def login(self, username):
        try:
            query = "SELECT password from users where username=%s"
            logging.info(f"query --> {query}")
            logging.info(f"username --> {username}")
            self.cursor.execute(query,username)
            result = self.cursor.fetchone()
            pass_hash = result.get("password")
        except Exception as e:
            logging.error(e)
            return e
        else:
            return pass_hash


