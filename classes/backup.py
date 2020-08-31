from psycopg2 import connect
from datetime import datetime
from secrets import token_urlsafe
import os
import csv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class Backup():

    def __init__(self,dbname,user,password,host,port):
        self.connnection = connect(dbname=dbname,user=user,password=password,host=host,port=port)
        self.cursor      = self.connnection.cursor()

    async def _select(self,table_name):
        query = "select * from {}".format(table_name)

        try:
            with self.connnection:
                self.cursor.execute(query)
                columns = [i[0] for i in self.cursor.description]
                result  = self.cursor.fetchall()

            return columns, result
        except Exception as e:
            return e,e



    async def backup(self,table_name):
        now = datetime.now()
        token = token_urlsafe(4)
        filename = '{0}_{1}_{2}_{3}_{4}_{5}_{6}_{7}.csv'.format(now.year,now.month,now.day,now.hour,now.minute,now.second,token,table_name)
        path = BASE_DIR + '/static/files/' + filename

        columns, result = await self._select(table_name)
        
        try:
            with open(path,'w') as w:
                writer = csv.writer(w)
                writer.writerow(columns)
                writer.writerows(result)

            return path
        except Exception as e:
            return 'static/img/error.png'