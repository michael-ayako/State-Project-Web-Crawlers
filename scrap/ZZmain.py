import pandas as pd
from termcolor import colored
import threading as th
import time

from scrap.course_name_scrap import course_names
from scrap.faculty_scrap import faculty
from scrap.courses_scrap import courses
from scrap.events_scrap import events



class scrap_handler():
    def __init__(self, logger):
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
            print('Fetching faculty information...')
            faculty(self.logger).__main__()

    def courses_scrap(self):
        print()
        print(colored("Okay time to fetch course information", 'green'))
        try:
            pd.read_json('./data/course_data.json')
            print(colored('Seems we already have course information', 'yellow'))
        except:
            print('Fetching course information...')
            courses(self.logger).__main__()

    def event_scrap(self):
        print()
        print(colored("Okay time to fetch event information", 'green'))
        try:
            pd.read_json('./data/events_data.json')
            print(colored('Seems we already have event information', 'yellow'))
        except:
            print('Fetching event information...')
            events(self.logger).__main__()

    def __main__(self):
        self.event_scrap()
        t1 = th.Thread(target=self.course_name_scrap(), name = 'course_name_scrap')
        t1.start()
        t1.join()

        t2 = th.Thread(target=self.faculty_scrap(), name = 'faculty_scrap')
        t3 = th.Thread(target=self.courses_scrap(), name = 'courses_scrap')
        t4 = th.Thread(target=self.event_scrap(), name = 'event_scrap')
        t2.start()
        t3.start()
        t4.start()
        t2.join()
        t3.join()
        t4.join()



