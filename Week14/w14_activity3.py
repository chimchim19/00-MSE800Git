""" Week 14 Activity 3: Web scraping """

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    url = 'https://commeventshub.onrender.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    events = soup.find_all('div', class_ = 'card-body')
    #print(events)

    event_counter = 0
    for event in events:
        event_counter += 1
        #print(event_counter)
        #print(event)

    print(f"\nThere are {event_counter} upcoming events listed.\n")
