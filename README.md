# Polish_cyclists_results_review
## Overview
The app is designed for cycling fans to daily track the results of Polish cyclists (men and women). It scrapes standings from [First Cycling](https://firstcycling.com/), filters them to display only Polish riders, and then saves this information into a relational PostgreSQL database. You can run the app daily to maintain a complete database of Polish cyclists' results over the last period. Once the initial database is created (a script is provided for this), subsequent runs of the main program will update it. The database follows Kimball's dimensional modeling techniques.

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
  




