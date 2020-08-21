from mysql import connector as mysql
from static import static
import pandas as pd
from tqdm import tqdm
import re

class database_load:
    def __init__(self):
        self.subject_name_data = []
        self.faculty_data = []
        self.course_data = []
        self.events_data = []

    def load_course_names(self):
        static_ = static()
        try:
            cnx = mysql.connect(host=static_.host,
                                user=static_.user,
                                passwd=static_.password,
                                db=static_.database)
            cursor = cnx.cursor(buffered=True)
            size = (self.subject_name_data.abbrev).size
            for x in tqdm(range(size)):
                abbrev = self.subject_name_data['abbrev'][x].replace("\'", "%").replace('\"', '$')
                fullname = self.subject_name_data['fullname'][x].replace("\'", "%").replace('\"', '$')
                load_query = "INSERT INTO subject_abrv_to_full (abrev, full) VALUES ('{}', '{}')".format(abbrev,fullname)
                check_query = "SELECT * FROM subject_abrv_to_full where abrev = '{}'".format(abbrev)
                cursor.execute(check_query)
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(load_query)
            cnx.commit()
            cnx.close()
        except Exception as err:
            cnx.rollback()
            print('Error: {}'.format(err))

    def load_faculty(self):
        static_ = static()
        try:
            cnx = mysql.connect(host=static_.host,
                                user=static_.user,
                                passwd=static_.password,
                                db=static_.database)
            cursor = cnx.cursor(buffered=True)
            size = (self.faculty_data.name).size
            for x in tqdm(range(size)):
                name = self.faculty_data['name'][x]
                firstname = name.split()[0]
                lastname = name.split()[1]
                title = self.faculty_data['title'][x].strip()
                dept = self.faculty_data['dept'][x].strip()
                email = self.faculty_data['email'][x]
                phone = self.faculty_data['phone'][x].strip()
                campus = self.faculty_data['campus_id'][x]
                if phone == "":
                    phone = 0
                else:
                    phone = re.sub(r"[()-]", "", phone)

                check_query = ('SELECT * FROM faculty WHERE email = "{}";'.format(email))
                load_query = ('INSERT INTO faculty (firstname,lastname,department,title,email,phone,campus_id)'
                              'VALUES("{}","{}","{}","{}","{}","{}","{}");'.format(firstname, lastname, dept, title,
                                                                              email, phone, campus))

                cursor.execute(check_query)
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(load_query)
            cnx.commit()
            cnx.close()
        except Exception as err:
            cnx.rollback()
            print('Error: {}'.format(err))

    def load_courses(self):
        static_ = static()
        try:
            cnx = mysql.connect(host=static_.host,
                                user=static_.user,
                                passwd=static_.password,
                                db=static_.database)
            cursor = cnx.cursor(buffered=True)
            size = self.course_data.id.size
            for x in tqdm(range(size)):
                subject = self.course_data['subj'][x]
                number = self.course_data['number'][x]
                name = self.course_data['title'][x].replace("\'", "%").replace('\"', '$')
                description = self.course_data['description'][x].replace("\'", "%").replace('\"', '$')
                url = self.course_data['urls'][x]
                campus_id = self.course_data['campus_id'][x]
                instructor = self.course_data['instructor'][x].replace("\'", "%").replace('\"', '$')
                semester = self.course_data['yrtr'][x]

                check_query = "SELECT * FROM course where subject = '{}' AND number ='{}' AND campus_id = '{}' AND" \
                              " semester = '{}'".format(subject,number, campus_id, semester)
                load_query = "INSERT INTO course (subject,number,name,description,url,campus_id,instructor,semester)" \
                             "VALUES('{}','{}','{}','{}','{}','{}','{}','{}')" \
                    .format(subject, number, name, description, url, campus_id, instructor, semester)
                cursor.execute(check_query)
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(load_query)
            cnx.commit()
            cnx.close
        except Exception as err:
            cnx.rollback()
            print('Error: {}'.format(err))

    def load_events(self):
        static_ = static()
        try:
            cnx = mysql.connect(host=static_.host,
                                user=static_.user,
                                passwd=static_.password,
                                db=static_.database)
            cursor = cnx.cursor(buffered=True)
            size = self.events_data.campus_id.size
            for x in tqdm(range(size)):
                campus_id = self.events_data['campus_id'][x]
                title = self.events_data['title'][x]
                url = self.events_data['url'][x]
                date = self.events_data['date'][x]

                check_query = "SELECT * FROM events WHERE campus_id = '{}' AND title = '{}' AND url = '{}' AND " \
                              "date = '{}'".format(campus_id, title, url, date)
                load_query = "INSERT INTO events (campus_id,title,url,date) VALUES('{}', '{}', '{}','{}')"\
                    .format(campus_id, title, url, date)

                cursor.execute(check_query)
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(load_query)
            cnx.commit()
            cnx.close
        except Exception as err:
            cnx.rollback()
            print('Error: {}'.format(err))

    def load_sections(self):
        static_ = static()
        try:
            cnx = mysql.connect(host=static_.host,
                                user=static_.user,
                                passwd=static_.password,
                                db=static_.database)
            cursor = cnx.cursor(buffered=True)
            size = self.course_data.id.size
            for x in tqdm(range(size)):
                number = self.course_data.sec[x]
                campus_id = self.course_data.campus_id[x]
                term = self.course_data.term[x]
                course_subject = self.course_data.subj[x]
                course_number = self.course_data.number[x]
                year = self.course_data.year[x]
                url = self.course_data.urls[x]

                dtype_check = lambda a : a if type(a) == "<class 'int'>" else 0
                credits = dtype_check(self.course_data.crd[x])
                offered_through = self.course_data.offered_through[x]
                campus = self.course_data.campus[x]
                location = self.course_data.location[x]
                res_tuition = dtype_check(self.course_data.res_tuition[x])
                non_res_tuition = dtype_check(self.course_data.non_res_tuition[x])
                fees = dtype_check(self.course_data.fees[x])
                description = self.course_data.description[x].replace("\'", "%").replace('\"', '$')

                check_query = "SELECT * FROM section WHERE campus_id = '{}' AND course_subject = '{}' AND " \
                              "course_subject = '{}' AND term = '{}'".format(campus_id, course_subject, course_number,
                                                                         term)
                load_query = "INSERT INTO section (number, campus_id, term, course_subject, course_number, year, url, " \
                             "credits, offered_through, campus, location, resident_tuition, nonresident_tuition, fees, " \
                             "description) VALUES('{}', '{}', '{}','{}', '{}', '{}','{}' ,'{}', '{}','{}', '{}', '{}'," \
                             "'{}', '{}', '{}')"\
                    .format(number, campus_id, term, course_subject, course_number, year, url, credits ,offered_through,
                            campus, location, res_tuition, non_res_tuition, fees,description)

                cursor.execute(check_query)
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(load_query)

            cnx.commit()
            cnx.close
        except Exception as err:
            cnx.rollback()
            print('Error: {}'.format(err))



    def __main__(self):
        try:
            print('loading course names to database...')
            self.subject_name_data = pd.read_json('./data/subject_name_data.json')
            self.load_course_names()
            print('loading faculty information to database...')
            self.faculty_data = pd.read_json('./data/faculty_data.json')
            self.load_faculty()
            print('loading course information to database...')
            self.course_data = pd.read_json('./data/course_data.json')
            self.load_courses()
            print('loading section information to database...')
            self.load_sections()
            print('loading event data to database')
            self.events_data = pd.read_json('./data/events_data.json')
            self.load_events()

        except Exception as err:
            print("Error: {}".format(err))