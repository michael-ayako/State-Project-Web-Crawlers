from mysql import connector as mysql
from static import static
import pandas as pd
from termcolor import colored
from tqdm import tqdm
import re


class load_times_table:
    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def conn():
        static_ = static()
        cnx = mysql.connect(host=static_.host,
                            user=static_.user,
                            passwd=static_.password,
                            db=static_.database)
        return cnx

    def update(self):
        pass

    @staticmethod
    def _day(day):
        days = []
        if day != 'n/a':
            day = day.split()
            for x in day:
                switcher = {"M": "Monday", "T": "Tuesday", "W": "Wednesday", "Th": "Thursday", "F": "Friday",
                            "Sa": "Saturday", "Su": "Sunday", "n/a": "N/A"
                            }
                if switcher[x] in days:
                    pass
                else:
                    days.append(switcher[x])
            return days
        elif day == 'n/a':
            days.append(day)
            return days

    @staticmethod
    def _date(dates):
        month = dates.split('/')[0]
        date = dates.split('/')[1]
        return "{}/{}".format(month, date)

    @staticmethod
    def fetch_section_id(course_subject, course_number, campus_id, semester):
        query = "SELECT section_id FROM section " \
                "WHERE course_subject = '{}' AND course_number = '{}' AND campus_id = '{}' AND semester = '{}'" \
            .format(course_subject, course_number, campus_id, semester)

        return query

    @staticmethod
    def data_check(section, days):
        query = "SELECT * FROM times where section_id = '{}' AND days = '{}'" \
            .format(section, days)
        return query

    @staticmethod
    def insert(startdate, enddate, starttime, endtime, section_id, days, campus_id):
        query = "INSERT INTO times  (startdate, enddate, starttime, endtime, section_id, days,  campus_id) " \
                "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}' )" \
            .format(startdate, enddate, starttime, endtime, section_id, days, campus_id)
        return query

    def __main__(self):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(buffered=True)
            data = pd.read_json('./data/course_data.json')
            size = data.id.size

            for x in tqdm(range(size)):
                course_subject = data['subj'][x]
                course_number = data['number'][x]
                campus_id = data['campus_id'][x]
                semester = data['yrtr'][x]
                dates = data['dates'][x]
                startdate = "{}/{}".format(data['year'][x], self._date(dates.split("-")[0].strip()))
                enddate = "{}/{}".format(data['year'][x], self._date(dates.split("-")[1].strip()))
                days = self._day(data['day'][x])
                times = data ['times'][x].strip()
                for dayz in days:
                    if times != "n/a":
                        starttime = times.split("-")[0].strip()
                        endtime = times.split("-")[1].strip()
                    else:
                        starttime = "00:00"
                        endtime = "00:00"
                    cursor.execute(self.fetch_section_id(course_subject, course_number, campus_id, semester))
                    j = cursor.fetchone()
                    section_id = j[0]
                    cursor.execute(self.data_check(section_id, dayz))
                    m = cursor.fetchone()
                    if m==None:
                        cursor.execute(self.insert(startdate, enddate, starttime, endtime, section_id, dayz ,campus_id))
            cnx.commit()
            cnx.close()
        except Exception as expt:
            self.logger.warning("Error: {}".format(expt))
