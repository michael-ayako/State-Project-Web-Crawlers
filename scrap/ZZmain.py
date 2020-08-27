import pandas as pd
from termcolor import colored

from scrap.course_name_scrap import course_names
from scrap.faculty_scrap import faculty
from scrap.courses_scrap import courses
from scrap.scrap_events import events



class scrap_handler:
    def __init__(self,logger):
        self.logger = logger

    def course_name_scrap(self):
        print()
        print(colored("Let's start this by fetching course names", 'green'))
        try:
            pd.read_json('./data/subject_name_data.json')
            print(colored("Seems we have course name information already", 'yellow'))
        except:
            print(colored('Fetching Subject Names...', 'blue'))
            course_names(self.logger).__main__()

    def faculty_scrap(self):
        print()
        print(colored("Okay time to fetch faculty information", 'green'))
        try:
            pd.read_json('./data/faculty_data.json')
            print(colored('Seems we already have faculty information', 'yellow'))
        except:
            print('Fetching Subject Names...')
            faculty(self.logger).__main__()

    def courses_scrap(self):
        print()
        print(colored("Okay time to fetch course information", 'green'))
        try:
            pd.read_json('../data/course_data.json')
            print(colored('Seems we already have course information', 'yellow'))
        except:
            print('Fetching course information...')
            courses(self.logger).__main__()

    def __main__(self):
        self.course_name_scrap()
        self.faculty_scrap()
        self.courses_scrap()

