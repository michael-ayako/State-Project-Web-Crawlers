from scrap.course_name_scrap import course_names
from scrap.faculty_scrap import faculty
from scrap.courses_scrap import courses
from scrap.scrap_events import events
import pandas as pd

class scrap_handler:
    def __init__(self,logger):
        self.logger = logger

    def course_name_scrap(self):
        print("Let's start this by fetching course names")
        self.logger.info("Checking Subject Name Data")
        try:
            self.subject_name_data = pd.read_json('../data/subject_name_data.json')
            print("Seems we already have this in place")
            self.logger.info("Subject name data is already available")
        except:
            self.logger.info("Subject Name Data Unavailable at this point")
            print('Fetching Subject Names...')
            cn = course_names(self.logger)
            cn.__main__()


    def __main__(self):
        self.course_name_scrap()
