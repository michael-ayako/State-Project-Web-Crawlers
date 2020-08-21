from bs4 import BeautifulSoup
import requests
import pandas as pd

from tqdm import tqdm

class events:
    def __init__(self):
        self.events_data = []

    def fetch_events(self):
        # website: website link
        # Metrostate events
        website = "https://www.metrostate.edu/calendar?page="
        # page: page number
        page = 3
        # infinite loop
        event_data = []
        while (page > 0):
            # fetch html page
            website_html = BeautifulSoup(requests.get(website + "/calendar?page=" + str(page)).content, "html.parser")
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

        self.events_data = pd.DataFrame(data=event_data, columns=['campus_id', 'title', 'url', 'date'])
        self.events_data.to_json('./data/events_data.json')

    def __main__(self):
        try:
            self.events_data = pd.read_json('./data/events_data.json')
        except:
            print("Fetching Event Data....")
            self.fetch_events()
