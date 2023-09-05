from bs4 import BeautifulSoup
from datetime import datetime
import requests

# Extracting race links from main site
def extract_race_links():
    home_html = requests.get("https://firstcycling.com/").text
    soup = BeautifulSoup(home_html, "lxml")
    race_links = []
    current_day = datetime.today().strftime("%B") + str(datetime.today().day)
    #current_day = "September3"
    fc_current_day = soup.find('div', id=current_day)
    race_refs = fc_current_day.find_all('a', title="Results")          # for particular day
    #race_refs = soup.find_all('a', title="Results")                     # for all days
    for race_ref in race_refs:
        race_links.append(race_ref.get('href'))
    return race_links

# Collecting data from the site
def extract_results(race_links):
    results_list = []
    for race_link in race_links:
        race_html = requests.get("https://firstcycling.com/" + race_link).text
        soup = BeautifulSoup(race_html, "lxml")
        standings = soup.find("div", class_="tab-content results")
        cyclists = standings.find_all("tr")
        for cyclist in cyclists:
            if cyclist.find("span", class_="flag flag-pl"):
                race = soup.h1.text
                cyclist_name = cyclist.a['title']
                rank = cyclist.td.string
                race, cyclist_name = race.replace("\'", " "), cyclist_name.replace("\'", " ") # to avoid sql bugs
                time = cyclist.contents[-2].string
                if time:
                    time = time.replace(' ', '')
                results_list.append((cyclist_name, race, rank, time))
    return results_list