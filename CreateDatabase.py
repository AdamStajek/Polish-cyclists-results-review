from psycopg2 import connect

def createDatabase(name, user, password):
    conn = connect(f'user={user} password={password}')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f' DROP DATABASE IF EXISTS \"{name}\";')
    cursor.execute(f'create database {name}')
    database_connection = connect(database = name, user='postgres', password='postgres')
    database = database_connection.cursor()
    database.execute("""CREATE TABLE IF NOT EXISTS public.\"Results\"(
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
            cyclist_fk integer,
            race_fk integer,
            rank character varying(10),
            \"time\" character varying(10),
            CONSTRAINT \"Results_pkey\" PRIMARY KEY (id))""")

    database.execute("""CREATE TABLE IF NOT EXISTS public.cyclists(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(100),
    CONSTRAINT cyclists_pkey PRIMARY KEY (id))""")

    database.execute("""CREATE TABLE IF NOT EXISTS public.races(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    race_name character varying(100),
    CONSTRAINT races_pkey PRIMARY KEY (id))""")

    database_connection.commit()
    database_connection.close()