from Classes.RaceLinksExtraction import RaceLinksExtraction
from Classes.ResultsExtraction import ResultsExtraction
from Classes.DatabaseInsertion import DatabaseInsertion
from psycopg2 import connect


def main(name, user, password):
    race_links_extraction, results_extraction, insertion = createObjectInstances()
    cursor = connect(name, user, password)
    race_links = race_links_extraction.extractRaceLinks()
    results_list = results_extraction.extractResults(race_links)
    insertion.insertData(cursor, results_list)


def createObjectInstances():
    return RaceLinksExtraction(), ResultsExtraction(), DatabaseInsertion()

def connect(name, user, password):
    conn = connect(database=name, user=user, password=password)
    conn.autocommit = True
    return conn.cursor()


if __name__ == "__main__":
    main("abc", "postgres", "postgres")

