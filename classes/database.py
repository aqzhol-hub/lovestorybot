from psycopg2 import connect
# from constant import *

dbname = 'puttgvir'
user = 'puttgvir'
password = 'scuWJvr8CgsuGpkzgyC3YBsHVdz7cbED'
host = 'rogue.db.elephantsql.com'
port = '5432'

class Database():

    # --------Constructor
    def __init__(self,dbname,user,password,host,port):

        self.connection = connect(dbname = dbname, user = user, password = password, host = host, port = port)
        self.cursor = self.connection.cursor()

    
    # --------Public methods
    def add_client(self,chat_id,first_name,last_name,username):

        try:
            with self.connection:
                self.cursor.execute("insert into Client(chat_id,first_name,last_name,username) values(%s,%s,%s,%s) on conflict do nothing", (chat_id,first_name,last_name,username))
                self.connection.commit()
        except Exception as e:
            print(e)

    def add_client_liking(self,chat_id,variation_name):

        try:
            with self.connection:
                self.cursor.execute("insert into Client_has_Variation(quiz_id,variation_id) values(%s,%s)", (self.__quiz_id(chat_id),self.__variation_id(variation_name)))
                self.connection.commit()
        except Exception as e:
            print(e)

    def add_quiz(self,chat_id):

        try:
            with self.connection:
                self.cursor.execute("insert into Quiz(client_id) values (%s)",[self.__client_id(chat_id)])
                self.connection.commit()
        except Exception as e:
            print(e)

    def quiz_result(self,chat_id):

        try:
            with self.connection:
                query = "select variation_name from Variation where variation_id in (select variation_id from Client_has_Variation where quiz_id = %s)"
                # self.cursor.execute("select variation_id from Client_has_Variation where quiz_id = %s", [self.__quiz_id(chat_id)])
                self.cursor.execute("select variation_name from Variation where variation_id in (select variation_id from Client_has_Variation where quiz_id = %s)", [self.__quiz_id(chat_id)])
                return self.cursor.fetchall()
        except Exception as e:
            print(e)
    
        

    # --------Private methods
    def __variation_id(self,variation_name):
        
        try:
            with self.connection:
                self.cursor.execute("select variation_id from Variation where variation_name = %s", [variation_name])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)
        

    def __quiz_id(self,chat_id):

        try:
            with self.connection:
                self.cursor.execute("select max(quiz_id) from Quiz where client_id = %s",[self.__client_id(chat_id)])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)

    def __category_id(self, variation_name):

        try:
            with self.connection:
                self.cursor.execute("select category_id from Category where category_name = %s", [self.__category_name(variation_name)])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)
        
    def __client_id(self, chat_id):

        try:
            with self.connection:
                self.cursor.execute("select client_id from Client where chat_id = %s", [chat_id])
                return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)

    def __category_name(self,variation_name):

        values = list(variations.values())
        keys = list(variations.keys())
        return keys[values.index([i for i in values if variation_name in i][0])]

d = Database(dbname,user,password,host,port)