from bs4 import BeautifulSoup
import requests


#extract list of race links in the past 3 days
home_html = requests.get("https://firstcycling.com/").text
soup = BeautifulSoup(home_html, "lxml")
date_container = soup.find("div", id="tabs-container")
dates = date_container.find_all("div", class_="tab-content")
race_links = []
for date in dates:
    race_refs = date.find_all('a', title="Results")
    for race_ref in race_refs:
        race_links.append(race_ref.get('href'))


for race_link in race_links:
    race_html = requests.get("https://firstcycling.com/" + race_link).text
    soup = BeautifulSoup(race_html, "lxml")
    standings = soup.find("div", class_="tab-content results")
    cyclists = standings.find_all("tr")
    print(soup.h1.text)
    for cyclist in cyclists:
        if cyclist.find("span", class_="flag flag-pl"):
            if cyclist.td.string == "DNF" or cyclist.td.string == "DNS":
                print(f"{cyclist.td.string} {cyclist.a['title']}")
            else:
                print(f"{cyclist.td.string}. {cyclist.a['title']} {cyclist.contents[-2].string.replace(' ', '')}")


