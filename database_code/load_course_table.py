from mysql import connector as mysql
from static import static
import pandas as pd
from termcolor import colored
from tqdm import tqdm
import re

class load_course_table:
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

    def data_check(self, subject,number, campus_id, semester):
        query = "SELECT * FROM course where subject = '{}' AND number ='{}' AND campus_id = '{}' AND" \
                              " semester = '{}'".format(subject,number, campus_id, semester)
        return query

    def insert(self, subject, number, name, description, url, campus_id,  semester):
        query = "INSERT INTO course (subject,number,name,description,url,campus_id,semester)" \
                             "VALUES('{}','{}','{}','{}','{}','{}','{}')" \
            .format(subject, number, name, description, url, campus_id,  semester)
        return query

    def __main__(self):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(buffered=True)
            data = pd.read_json('./data/course_data.json')
            size = data.campus_id.size
            for x in tqdm(range(size)):
                subject = data['subj'][x]
                number = data['number'][x]
                name = data['title'][x].replace("\'", "%").replace('\"', '$')
                description = data['description'][x].replace("\'", "%").replace('\"', '$')
                url = data['urls'][x]
                campus_id = data['campus_id'][x]
                semester = data['yrtr'][x]

                cursor.execute(self.data_check(subject,number, campus_id, semester))
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(self.insert(subject, number, name, description, url, campus_id, semester))
            cnx.commit()
            cnx.close()
        except Exception as err:
            print(colored('Error discovered loading faculty table', 'red'))
            self.logger.warning("/database_code/ZZmain/load_course_table: {}".format(err))
