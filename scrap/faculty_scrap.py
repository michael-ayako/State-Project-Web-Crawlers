from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

class faculty:
    def __init__(self,logger):
        self.logger = logger

    def fetch_faculty(self):
        number_of_pages = 100
        faculty_data = []
        base_url = "https://www.metrostate.edu/about/directory?full=&fname=&name=&dpt=&page="
        for x in tqdm(range(number_of_pages)):
            url = base_url+str(x)
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'html.parser')
            try:
                table = soup.find('table')
                t_body = table.find('tbody')
                tr = t_body.find_all('tr')
                if tr != '':
                    for x in tr:
                        td = x.find_all('td')
                        name = td[0].find('a').text
                        link = "https://www.metrostate.edu{}".format(td[0].find('a').get('href'))
                        title = td[1].text
                        dept = td[2].text
                        email = td[3].text
                        phone = td[4].text
                        campus_id = '076'
                        faculty_data.append([name,title,dept,email,phone,campus_id,link])
                else:
                    break
            except:
                break
        return faculty_data


    def __main__(self):
        data = []
        err = True
        try:
            data = self.fetch_faculty()
        except Exception as expt:
            err = False
            self.logger.critical("Error: {}".format(expt))
        finally:
            if err == True:
                frame = pd.DataFrame(data=data, columns=['name', 'title', 'dept', 'email', 'phone',
                                                                             'campus_id', 'link'])
                frame.to_json('./data/faculty_data.json')
                self.logger.info("faculty_scrap script worked fine")
            else:
                self.logger.info("course_name_scrap failed")
                print("An error was noticed in the script. Program shall be terminating")

