import requests
from bs4 import BeautifulSoup

class ResultsExtractor:

    def extractResults(self, race_links):
        polish_result_list = []
        for race_link in race_links:
            BSInstance = self.createRaceBSInstance(race_link)
            cyclists = self.findAllResults(BSInstance)
            for cyclist in cyclists:
                if self.isPolish(cyclist):
                    polish_result = self.getPolishResult(cyclist, BSInstance)
                    polish_result_list.append(polish_result)
        return polish_result_list

    def createRaceBSInstance(self, race_link):
        race_html = self.getRaceHtml(race_link)
        return BeautifulSoup(race_html, "lxml")

    def getRaceHtml(self, race_link):
        return requests.get("https://firstcycling.com/" + race_link).text

    def findAllResults(self, BSInstance):
        results = BSInstance.find("div", class_="tab-content results")
        return results.find_all("tr")

    def isPolish(self, cyclist):
        return cyclist.find("span", class_="flag flag-pl") is not None

    def getPolishResult(self, cyclist, BSInstance):
        race = self.getRaceName(BSInstance)
        name = self.getCyclistName(cyclist)
        rank = self.getCyclistRank(cyclist)
        time = self.getCyclistTime(cyclist)
        race, name, time = self.formatScrapedData(race, name, time)
        return [name, race, rank, time]

    def getRaceName(self, BSInstance):
        return BSInstance.h1.text

    def getCyclistName(self, cyclist):
        return cyclist.a['title']

    def getCyclistRank(self, cyclist):
        return cyclist.td.string

    def getCyclistTime(self, cyclist):
        return cyclist.contents[-2].string

    def formatScrapedData(self, race, cyclist_name, time):
        return race.replace("\'", " "), cyclist_name.replace("\'", " "), time.replace(' ', '') if time else None
