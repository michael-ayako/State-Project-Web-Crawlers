from termcolor import colored

from database_code.load_events_table import load_events_table
from database_code.load_subject_abrv_to_full_table import load_subject_abrv_to_full_table
from database_code.load_faculty_table import load_faculty_table
from database_code.load_course_table import load_course_table
from database_code.load_section_table import load_section_table

class database_handler:
    def __init__(self, logger):
        self.logger = logger

    def __main__(self):
        print()
        print("Loading data to the database")
        print(colored("Let's start by loading event data", 'green'))
        load_events_table(self.logger).__main__()
        print()
        print(colored("Loading subject_abrv_to_full table", 'green'))
        load_subject_abrv_to_full_table(self.logger).__main__()
        print()
        print(colored("Loading faculty table", 'green'))
        load_faculty_table(self.logger).__main__()
        print()
        print(colored("Loading course table", 'green'))
        load_course_table(self.logger).__main__()
        print()
        print(colored("Loading section table", 'green'))
        load_section_table(self.logger).__main__()