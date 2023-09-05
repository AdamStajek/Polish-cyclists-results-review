from bs4 import BeautifulSoup
from datetime import datetime
import requests
import psycopg2

# connecting with database
conn = psycopg2.connect("dbname = First_Cycling user=postgres password=postgres")
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("TRUNCATE TABLE public.\"Results\" RESTART IDENTITY")
cursor.execute("TRUNCATE TABLE public.cyclists RESTART IDENTITY")

# extract list of race links in the past 3 days
home_html = requests.get("https://firstcycling.com/").text
soup = BeautifulSoup(home_html, "lxml")
race_links = []
# current_day = datetime.today().strftime("%B") + str(datetime.today().day)
current_day = "September3"
fc_current_day = soup.find('div', id=current_day)
race_refs = fc_current_day.find_all('a', title="Results")
for race_ref in race_refs:
    race_links.append(race_ref.get('href'))

# extract polish riders from results
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
            cursor.execute(f"INSERT INTO public.cyclists VALUES (DEFAULT, \'{cyclist_name}\')")
            if cyclist.td.string == "DNF" or rank == "DNS" or cyclist.td.string == "OOT":
                #print(f"{race},{cyclist_name}, {rank}")
                cursor.execute(f"INSERT INTO public.\"Results\" VALUES (DEFAULT, \'{race}\', \'{cyclist_name}\', \'{rank}\', \'NULL\')")
            else:
                time = cyclist.contents[-2].string.replace(' ','')
                #print(f"{race},{cyclist_name},{rank}.,{time}")
                cursor.execute(f"INSERT INTO public.\"Results\" VALUES (DEFAULT, \'{race}\', \'{cyclist_name}\', \'{rank}.\', \'{time}\')")


