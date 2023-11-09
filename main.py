from RaceLinksExtraction import RaceLinksExtraction
from CreateDatabase import truncateTable, connect, createDatabase
from ResultsExtraction import ResultsExtraction
from DatabaseInsertion import DatabaseInsertion


def main():
    race_links_extraction, results_extraction, insertion = createObjectInstances()
    database = connect()
    createDatabase("abc",database)

    race_links = race_links_extraction.extractRaceLinks()
    #results_list = results_extraction.extractResults(race_links)
    # TODO delete truncation after tests
    #truncateTable(database)
    #insertion.insertData(database, results_list)


def createObjectInstances():
    return RaceLinksExtraction(), ResultsExtraction(), DatabaseInsertion()


if __name__ == "__main__":
    main()

