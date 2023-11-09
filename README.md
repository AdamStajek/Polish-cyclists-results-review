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
Download and install PostgreSQL from [PostgreSQL](https://www.postgresql.org/download/), then create PostgreSQL server on your computer and memorize username along with password.

### Run the app
- if you want to create or clean your database (mandatory only before first use):
  ``` bash
  cd FirstCycling
  python createDatabase.py name username password
  ```
  where:
  - name is the name of the database which will be created
  - username is username to your Postgres server
  - password is password to your Postgres server

- if you want to update or have a first commit to your database:
  ``` bash
  cd FirstCycling
  python main.py name username password
  ```
  where:
  - **name** is the name of previously created database
  - **username** is username to your Postgres server
  - **password** is password to your Postgres server
  




