from bs4 import BeautifulSoup
import requests
import pandas as pd

from tqdm import tqdm

class events:
    def __init__(self, logger):
        self.logger = logger

    def fetch_events(self):
        # website: website link
        # Metrostate events
        website = "https://www.metrostate.edu/calendar?page="
        # page: page number
        page = 1
        # infinite loop
        event_data = []
        for x in tqdm(range(page)):
            # fetch html page
            website_html = BeautifulSoup(requests.get(website + "/calendar?page=" + str(x)).content, "html.parser")
            # if data in page presents
            if not bool(
                    website_html.find('div', id='block-metrostate-content').find('div', class_='alert alert-warning')):
                # collect event data from page
                for event in website_html.find_all('div', class_="row metro--news-teaser metro--event-list"):
                    event_name = event.find('a').text
                    date_time = event.find('div', class_="d-block d-md-none metro-date-block")
                    date, time = date_time.find_all('time')
                    event_date = "{} {}".format(date.text, time.text)
                    event_link = website + event.find('a')['href']
                    campus_id = 76
                    event_data.append([campus_id,event_name,event_link,event_date])
            else:
                break
            page -= 1
        return event_data

    def __main__(self):
        data = []
        err = True
        try:
            data = self.fetch_events()
        except Exception as expt:
            err = False
            self.logger.critical("Error: {}".format(expt))
        finally:
            if err == True:
                frame = pd.DataFrame(data = data, columns=['campus_id', 'title', 'url', 'date'])
                frame.to_json('./data/events_data.json')
                self.logger.info("events_script script worked fine")
            else:
                self.logger.info("events_script failed")
                print("An error was noticed in the script. Program shall be terminating")


