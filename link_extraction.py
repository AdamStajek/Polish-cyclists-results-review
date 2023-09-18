from bs4 import BeautifulSoup
from datetime import *
import requests

class RaceLinksExtraction:
    def extractRaceLinks(self):
        race_refs = self.findRaceRefs()
        return self.createRaceLinks(race_refs)

    def findRaceRefs(self):
        FCHtml = self.getFCHtml()
        BSInstance = self.createBSInstance(FCHtml)
        current_date = self.getDate()
        TodayRacesHtml = self.findTodayRaces(BSInstance, current_date)
        return TodayRacesHtml.find_all('a', title="Results")

    def getFCHtml(self):
        return requests.get("https://firstcycling.com/").text

    def createBSInstance(self, fcHtml):
        return BeautifulSoup(fcHtml, "lxml")

    def getDate(self):
        return datetime.today().strftime("%B") + str(datetime.today().day)

    def findTodayRaces(self, BSInstance, current_date):
        return BSInstance.find('div', id=current_date)

    def createRaceLinks(self, race_refs):
        race_links = []
        for race_ref in race_refs:
            race_links.append(race_ref.get('href'))
        return race_links


