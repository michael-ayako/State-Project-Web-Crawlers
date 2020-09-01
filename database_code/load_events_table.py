from mysql import connector as mysql
from static import static
import pandas as pd
from termcolor import colored
from tqdm import tqdm
import re

class load_events_table:
    def __init__(self, logger):
        self.logger = logger

    def conn(self):
        static_ = static()
        cnx = mysql.connect(host=static_.host,
                            user=static_.user,
                            passwd=static_.password,
                            db=static_.database)
        return cnx

    def update(self):
        pass

    def data_check(self, campus_id, title, url, date):
        query = "SELECT * FROM events WHERE campus_id = '{}' AND title = '{}' AND url = '{}' AND " \
                      "date = '{}'".format(campus_id, title, url, date)
        return query

    def insert(self, campus_id, title, url, date):
        query = "INSERT INTO events (campus_id,title,url,date) VALUES('{}', '{}', '{}','{}')"\
                    .format(campus_id, title, url, date)
        return query

    def __main__(self):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(buffered=True)
            data = pd.read_json('./data/events_data.json')
            size = data.campus_id.size
            for x in tqdm(range(size)):
                campus_id = data['campus_id'][x]
                title = data['title'][x]
                url = data['url'][x]
                date = data['date'][x]

                cursor.execute(self.data_check(campus_id, title, url, date))
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(self.insert(campus_id, title, url, date))
            cnx.commit()
            cnx.close()
        except Exception as err:
            print(colored('Error discovered loading events table', 'red'))
            self.logger.warning("/database_code/ZZmain/load_events_table: {}".format(err))


