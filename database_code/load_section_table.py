from mysql import connector as mysql
from static import static
import pandas as pd
from termcolor import colored
from tqdm import tqdm


class load_section_table:
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

    def dtype_check(self, input):
        try:
            i = float(input)
            return i
        except:
            return 0



    def data_check(self, campus_id, course_subject, course_number, semester):
        query = "SELECT * FROM section WHERE campus_id = '{}' AND course_subject = '{}' AND " \
                "course_subject = '{}' AND semester = '{}'"\
            .format(campus_id, course_subject, course_number, semester)
        return query

    def insert(self, number, campus_id, term, course_subject, course_number, year, url, credits, offered_through,
                    campus, location, res_tuition, non_res_tuition, fees,description,semester):
        query = "INSERT INTO section (number, campus_id, term, course_subject, course_number, year, url," \
                "credits, offered_through, campus, location, resident_tuition, nonresident_tuition, fees, " \
                "description,semester) VALUES('{}', '{}', '{}','{}', '{}', '{}','{}' ,'{}', '{}','{}', '{}', '{}'," \
                "'{}', '{}', '{}','{}')"\
            .format(number, campus_id, term, course_subject, course_number, year, url, credits, offered_through,
                    campus, location, res_tuition, non_res_tuition, fees, description, semester)
        return query

    def __main__(self):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(buffered=True)
            data = pd.read_json('./data/course_data.json')
            size = data.campus_id.size
            for x in tqdm(range(size)):
                number = data.sec[x]
                campus_id = data.campus_id[x]
                term = data.term[x]
                course_subject = data.subj[x]
                course_number = data.number[x]
                year = data.year[x]
                url = data.urls[x]

                credits = self.dtype_check(data.crd[x])
                offered_through = data.offered_through[x]
                campus = data.campus[x]
                location = data.location[x]
                res_tuition = self.dtype_check(data.res_tuition[x])
                non_res_tuition = self.dtype_check(data.non_res_tuition[x])
                fees = self.dtype_check(data.fees[x])
                description = data.description[x].replace("\'", "%").replace('\"', '$')
                semester = data.yrtr[x]

                cursor.execute(self.data_check(campus_id, course_subject, course_number, semester))
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(self.insert(number, campus_id, term, course_subject, course_number, year,
                                               url, credits, offered_through,campus, location, res_tuition,
                                               non_res_tuition, fees, description,semester))
            cnx.commit()
            cnx.close()

        except Exception as err:
            print(colored('Error discovered loading section table', 'red'))
            self.logger.warning("/database_code/ZZmain/load_section_table: {}".format(err))