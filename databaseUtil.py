import logging
import json

from config import config
configObj = config()
log_dir = 'var/logs/errors.log'
logging.basicConfig(filename=log_dir,  format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)


class Util:

    def __init__(self):
        self.cursor = configObj.get_cursor()

    def getUsers(self):
        try:
            logging.info(f"before query")
            query = "SELECT username FROM app_users where status=1"
            logging.info(f"query --> {query}")
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            # file_name = results['file_name']
        except Exception as e:
            logging.error(e)
            return 'error'
        else:
            return results