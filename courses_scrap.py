from bs4 import BeautifulSoup
import requests
from static import static
import pandas as pd
from tqdm import tqdm
from course_name_scrap import course_names


class courses:
    def __init__(self):
        self.subject_name_data = []
        self.course_data = []
        self.course_details = []

    def rcid_constructor(self,len,campusid):
        if len == 3:
            return "0"+str(campusid)
        elif len == 2:
            return "00"+str(campusid)

    def makesearchpageurl(self, campusid, yrtr, subject):
        rcid = self.rcid_constructor(len(campusid),campusid)
        return "https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid={}" \
               "&searchrcid={}" \
               "&searchcampusid={}" \
               "&yrtr={}" \
               "&subject={}"\
               "&courseNumber=&courseId=&openValue=OPEN_PLUS_WAITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=" \
               "&mntransfer=&credittype=ALL&credits=&instructor=&keyword=&begindate=&site=&resultNumber=250"\
                   .format(campusid,rcid,campusid,yrtr,subject)

    def makecoursepageurls(self, campusid, yrtr, courseid):
        rcid = self.rcid_constructor(len(campusid), campusid)
        return "https://eservices.minnstate.edu/registration/search/detail.html?campusid={}" \
               "&courseid={}" \
               "&yrtr={}" \
               "&rcid={}" \
               "&localrcid={}" \
               "&partnered=false&parent=search"\
            .format(campusid, courseid, yrtr, rcid, rcid)


    def courseid_constructor(self, len, courseid):
        if len == 6:
            return str(courseid)
        elif len == 5:
            return "0"+str(courseid)
        elif len == 4:
            return "00"+str(courseid)
        elif len == 3:
            return "000"+str(courseid)
        elif len == 2:
            return "0000"+str(courseid)
        elif len == 1:
            return "00000"+str(courseid)


    def fetch_course_data(self):
        static_ = static()
        course_data, url, uri = [], [], []
        campuses = static_.campusid
        size = (self.subject_name_data.abbrev).size

        for campus in campuses:
            for x in range(size):
                if campus == int(self.subject_name_data['campus_id'][x]):
                    urls = self.makesearchpageurl(str(campus), str(static_.yrtr), self.subject_name_data['abbrev'][x])
                    url.append([urls, campus])

        print("Fetching course urls...")
        for urls, campus in tqdm(url):
            html_doc = requests.get(urls).content
            parsed = BeautifulSoup(html_doc, "html.parser")
            table = parsed.find_all('tbody')[1]
            table_rows = table.find_all('tr')
            for x in table_rows:
                id = x.find_all('td')[1].text.strip()
                yrtr = static_.yrtr
                link = self.makecoursepageurls(str(campus), yrtr, id)
                uri.append([link, campus])



        print("Fetching course data...")
        for urls, campus in tqdm(uri):
            try:
                html_doc = requests.get(urls).content
                parsed = BeautifulSoup(html_doc, "html.parser")
                table = parsed.find('table', class_='myplantable').find('tbody', class_='course-detail-summary') \
                    .find_all('td')
                id = table[1].text.strip()
                subj = table[2].text.strip()
                number = table[3].text.strip()
                sec = table[4].text.strip()
                title = table[5].text.strip()
                dates = table[6].text.strip()
                day = table[7].text.strip()
                times = table[8].text.strip()
                crd = table[9].text.strip()
                status = table[10].text.strip()
                instructor = table[11].text.strip()
                yrtr = static_.yrtr
                campus_id = campus

                # Sorting term data
                find_term = lambda a: "summer" if a == '1' else ("fall" if a == '3' else
                                                                 ("spring" if a == '5' else "j-term'"))
                term = find_term(str(yrtr)[4:])

                # Sorting out year data
                find_year = lambda a: int(a[:4])-1 if a[:4] == '1' \
                                            else (int(a[:4])-1 if a[4:] == '3'
                                            else (a[:4] if a == '5'
                                            else int(a[:4])-1))
                year = find_year(str(yrtr))

                offered_through = parsed.find_all('table', class_='meetingTable')[1].find_all('tr')[0] \
                    .find_all('td')[0].text.replace('Offered through:', '').strip()
                campus = parsed.find_all('table', class_='meetingTable')[1].find_all('tr')[1] \
                    .find_all('td')[0].text.replace('Campus:', '').strip()
                location = parsed.find_all('table', class_='meetingTable')[1].find_all('tr')[1] \
                    .find_all('td')[1].text.replace('Location:', '').strip()
                tuition = parsed.find('table', class_='plain fees')

                try:
                    res_tuition = tuition.find_all('tr')[0].find('td').text.replace('$', '').replace(',', '').strip()
                    non_res_tuition = tuition.find_all('tr')[1].find('td').text.replace('$', '').replace(',', '').strip()
                    fees = tuition.find_all('tr')[2].find('td').text.replace('$', '').replace(',', '').strip()

                    alldetails = parsed.find_all('div', class_='detaildiv')
                    description = alldetails[-1].next_sibling.replace('\t', '').replace('\n', '').strip()
                except:
                    res_tuition, non_res_tuition, fees, description = 'N/A', 'N/A', 'N/A', 'N/A'

                data = [id, subj, number, sec, term, year, title, dates, day, urls, times, crd, status, instructor,
                        offered_through, campus, location, res_tuition, non_res_tuition, fees, yrtr,
                        description, campus_id]
                course_data.append(data)
            except:
                pass



        self.course_data = pd.DataFrame(data=course_data,
                                        columns=['id', 'subj', 'number', 'sec', 'term', 'year', 'title', 'dates',
                                                 'day', 'urls', 'times', 'crd', 'status', 'instructor','offered_through',
                                                 'campus', 'location', 'res_tuition', 'non_res_tuition', 'fees',
                                                 'yrtr', 'description', 'campus_id'])
        self.course_data.to_json('./data/course_data.json')




    def __main__(self):
        try:
            self.subject_name_data = pd.read_json('./data/subject_name_data.json')
            self.course_data = pd.read_json('./data/course_data.json')
        except:
            if len(self.subject_name_data) == 0:
                print('fetching course names')
                cs = course_names()
                cs.fetch_course_names()
                self.subject_name_data = pd.read_json('./data/subject_name_data.json')
            if len(self.course_data) == 0:
                print('fetching course data...')
                self.fetch_course_data()
