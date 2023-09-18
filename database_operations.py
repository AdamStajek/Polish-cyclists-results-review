import psycopg2


def connectToDatabase():
    conn = psycopg2.connect("dbname = First_Cycling user=postgres password=postgres")
    conn.autocommit = True
    return conn.cursor()


def truncateTable(database):
    database.execute("TRUNCATE TABLE public.\"Results\" RESTART IDENTITY")
