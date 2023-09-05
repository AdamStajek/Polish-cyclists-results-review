import psycopg2
def connection():
    conn = psycopg2.connect("dbname = First_Cycling user=postgres password=postgres")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor