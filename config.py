import pymysql


class config:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'root'
        self.db = 'equipo'
        self.port = 3308
        self.connection = pymysql.connect( host= self.host,user= self.user, password= self.password,database= self.db,port= self.port, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor,autocommit=True)
        self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor

