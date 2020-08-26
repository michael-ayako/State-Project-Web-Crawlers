from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from tqdm import tqdm

class faculty:
    def __init__(self):
        self.faculty_data = []

    def fetch_faculty(self):
        number_of_pages = 100
        faculty_data = []
        base_url = "https://www.metrostate.edu/about/directory?full=&fname=&name=&dpt=&page="
        # for x in tqdm(range(number_of_pages)):
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
        self.faculty_data = pd.DataFrame(data=faculty_data, columns=['name', 'title', 'dept', 'email', 'phone',
                                                                    'campus_id','link'])
        self.faculty_data.to_json('./data/faculty_data.json')

    def __main__(self):
        try:
            os.mkdir('../data')
            print("Data folder created")
        except:
            pass
        try:
            self.faculty_data = pd.read_json('../data/faculty_data.json')
        except:
            print("Fetching faculty data...")
            self.fetch_faculty()