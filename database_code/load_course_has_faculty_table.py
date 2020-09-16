from mysql import connector as mysql
from static import static
import pandas as pd
from termcolor import colored
from tqdm import tqdm
import re

class load_course_has_faculty_table:
    def __init__(self, logger):
        self.logger = logger

    def conn(self):
        static_ = static()
        cnx = mysql.connect(host=static_.host,
                            user=static_.user,
                            passwd=static_.password,
                            db=static_.database)
        return cnx

    def find_faculty_id(self,firstname,lastname):
        query = "SELECT faculty_id FROM faculty where firstname = '{}' AND lastname = '{}'"\
            .format(firstname,lastname)
        return query

    def return_instructor(self, instructor):
        ins_arr = []
        firstname = instructor.split()[1::2]
        lastname = instructor.split()[0::2]

        if len(lastname) == len(firstname):
            for x in range(len(lastname)):
                fname = firstname[x].replace("\'", "%").replace(",", "")
                lname = lastname[x].replace("\'", "%").replace(",", "")
                ins_arr.append([fname, lname])
        return ins_arr

    def update(self):
        pass

    def insert(self, faculty_id, course_subject, course_number, campus_id, semester):
        query = "INSERT INTO course_has_faculty(faculty_id, course_subject, course_number, campus_id, semester)" \
                "VALUES('{}', '{}', '{}', '{}', '{}')"\
            .format(faculty_id, course_subject, course_number, campus_id, semester)
        return query

    def data_check(self, faculty_id, course_subject, course_number, campus_id, semester):
        query = "SELECT * FROM course_has_faculty WHERE faculty_id = '{}' AND  course_subject = '{}' AND " \
                "course_number = '{}' AND campus_id = '{}' AND semester = '{}'"\
            .format(faculty_id, course_subject, course_number, campus_id, semester)
        return query

    def __main__(self):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(buffered=True)
            data = pd.read_json('./data/course_data.json')
            size = data.id.size

            for x in tqdm(range(190, size)):
                course_subject = data['subj'][x]
                course_number = data['number'][x]
                campus_id = data['campus_id'][x]
                semester = data['yrtr'][x]
                instructor = data['instructor'][x]
                ins_arr = self.return_instructor(instructor)
                if(len(ins_arr)>0):
                    for x in ins_arr:
                        cursor.execute(self.find_faculty_id(x[0], x[1]))
                        j = cursor.fetchone()
                        if j!=None:
                            faculty_id = j[0]
                            cursor.execute(self.data_check(faculty_id, course_subject, course_number, campus_id, semester))
                            m = cursor.fetchone()
                            if m == None:
                                print(self.insert(faculty_id, course_subject, course_number, campus_id, semester))
                                cursor.execute(self.insert(faculty_id, course_subject, course_number, campus_id, semester))
            cnx.commit()
            cnx.close()
        except Exception as expt:
            self.logger.warning("Error: {}".format(expt))