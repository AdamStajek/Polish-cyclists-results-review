from link_extraction import RaceLinksExtraction
from database_operations import truncateTable, connectToDatabase
from results_extraction import ResultsExtractor
from database_insertion import Insertion


def main():
    race_links_extraction, results_extraction, insertion = createObjectInstances()
    database = connectToDatabase()
    race_links = race_links_extraction.extractRaceLinks()
    results_list = results_extraction.extractResults(race_links)
    # TODO delete truncation after tests
    truncateTable(database)
    insertion.insertData(database, results_list)


def createObjectInstances():
    return RaceLinksExtraction(), ResultsExtractor(), Insertion()


if __name__ == "__main__":
    main()

