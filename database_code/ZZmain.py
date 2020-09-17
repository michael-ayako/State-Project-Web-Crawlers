from termcolor import colored

from database_code.load_events_table import load_events_table
from database_code.load_subject_abrv_to_full_table import load_subject_abrv_to_full_table
from database_code.load_faculty_table import load_faculty_table
from database_code.load_course_table import load_course_table
from database_code.load_section_table import load_section_table
from database_code.load_times_table import load_times_table
from database_code.load_course_has_faculty_table import load_course_has_faculty_table

class database_handler:
    def __init__(self, logger):
        self.logger = logger

    def func_load_events_table(self):
        try:
            print(colored("Let's start by loading event data", 'green'))
            load_events_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def func_load_subject_abrv_to_full_table(self):
        try:
            print()
            print(colored("Loading subject_abrv_to_full table", 'green'))
            load_subject_abrv_to_full_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def func_load_faculty_table(self):
        try:
            print()
            print(colored("Loading faculty table", 'green'))
            load_faculty_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def func_load_course_table(self):
        try:
            print()
            print(colored("Loading course table", 'green'))
            load_course_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def func_load_section_table(self):
        try:
            print()
            print(colored("Loading course table", 'green'))
            load_section_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def func_load_section_table(self):
        try:
            print()
            print(colored("Loading course table", 'green'))
            load_section_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def func_load_course_has_faculty_table(self):
        try:
            print()
            print(colored("Loading course_has_faculty table", 'green'))
            load_course_has_faculty_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def func_load_times_table(self):
        try:
            print()
            print(colored("Loading times table", 'green'))
            load_times_table(self.logger).__main__()
        except Exception as excpt:
            print('Error : {}'.format(excpt))
            self.logger.warning('Error : {}'.format(excpt))

    def __main__(self):
        print()
        print("Loading data to the database")
        self.func_load_events_table()
        self.func_load_subject_abrv_to_full_table()
        self.func_load_faculty_table()
        self.func_load_course_table()
        self.func_load_section_table()
        self.func_load_times_table()
        self.func_load_course_has_faculty_table()
