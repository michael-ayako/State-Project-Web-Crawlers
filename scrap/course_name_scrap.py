from bs4 import BeautifulSoup
import requests
import pandas as pd
from static import static
from tqdm import tqdm
import sys

class course_names:
    def __init__(self, logger):
        self.logger = logger

    def campusid_constructor(self,len,campusid):
        if len == 3:
            return str(campusid)
        elif len == 2:
            return "0"+str(campusid)


    def fetch_course_names(self):
        campus_id = static()
        campuses = campus_id.campusid
        subjectnames = []
        for x in campuses:
            x = self.campusid_constructor(len(str(x)), x)
            url = 'https://eservices.minnstate.edu/registration/search/basic.html?campusid={}'.format(x)
            jsonlist = []
            subjectpage = requests.get(url)
            parsedpage = BeautifulSoup(subjectpage.text, 'html.parser')
            courses = parsedpage.find('select', id='subject').find_all('option')
            for course in tqdm(courses):
                abbrev = course['value']
                if abbrev == "":
                    pass
                else:
                    name = course.contents[0].split('(')[0].strip(' \n')
                    synonyms = []
                    jsondata = {}
                    jsondata['value'] = abbrev
                    synonyms.append(abbrev)
                    synonyms.append(abbrev.lower())
                    synonyms.append(name)
                    synonyms.append(name.lower())
                    jsondata['synonyms'] = synonyms
                    jsonlist.append(jsondata)
                    jsondata['original'] = name
            for i in jsonlist:
                subjectnames.append([i['value'], i['original'],x])

        return subjectnames



    def __main__(self):
        err = True
        try:
            data = self.fetch_course_names()
        except Exception as expt:
            err = False
            self.logger.critical("Error: {}".format(expt))
        finally:
            if err == True:
                frame = pd.DataFrame(data=data, columns=['abbrev', 'fullname', 'campus_id'])
                frame.to_json('./data/subject_name_data.json')
                self.logger.info("course_name_scrap script worked fine")
            else:
                self.logger.info("course_name_scrap failed")
                print("An error was noticed in the script. Program shall be terminating")
                sys.exit()