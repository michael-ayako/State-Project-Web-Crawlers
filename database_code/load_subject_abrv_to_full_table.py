from mysql import connector as mysql
from static import static
import pandas as pd
from termcolor import colored
from tqdm import tqdm
import re


class load_subject_abrv_to_full_table:
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

    def data_check(self, abbrev):
        query = "SELECT * FROM subject_abrv_to_full where abrev = '{}'"\
            .format(abbrev)
        return query

    def insert(self, abbrev, fullname):
        query = "INSERT INTO subject_abrv_to_full (abrev, full) VALUES ('{}', '{}')"\
            .format(abbrev, fullname)
        return query

    def __main__(self):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(buffered=True)
            data = pd.read_json('./data/subject_name_data.json')
            size = data.campus_id.size
            for x in tqdm(range(size)):
                abbrev = data['abbrev'][x].replace("\'", "%").replace('\"', '$')
                fullname = data['fullname'][x].replace("\'", "%").replace('\"', '$')
                cursor.execute(self.data_check(abbrev))
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(self.insert(abbrev, fullname))
        except Exception as err:
            print(colored('Error discovered loading subject_abrv_to_full table', 'red'))
            self.logger.warning("/database_code/ZZmain/load_subject_subject_abrv_to_full_table: {}".format(err))
