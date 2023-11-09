# Polish_cyclists_results_review
The app for cycling fans to follow the results of polish cyclists(men and women) every day. 
It scraps standings from [First Cycling](https://firstcycling.com/), filters them to show only polish riders and saves them into the relational postgresql database. You can run it every day to have a complete database of the results of polish cyclists over last period. Once you create a database (there is a script for that), it will be updated with every run of the main program. The database is created in accordance with the Kimball's dimensional modeling techniques.

**Modules used**:
- **BeautifulSoup4** is used to scrap data from FirstCycling
- **psycopg2** establishes the connection with database
- **requests** downloads FirstCycling html
- **datetime.time** gets today's date

### Instalation
``` bash
pip install BeautifulSoup psycopg2 requests datetime
```

### Run the app



