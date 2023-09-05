from extraction import *
from connection import *
from database_insertion import *


def main():
    cursor = connection()                                                # connecting with database
    race_links = extract_race_links()                                    # extract race links
    results_list = extract_results(race_links)                           # extract polish riders from results
    cursor.execute("TRUNCATE TABLE public.\"Results\" RESTART IDENTITY") # truncate table (to remove after tests)
    insertion(results_list, cursor)                                      # insertion into database



if __name__ == "__main__":
    main()
