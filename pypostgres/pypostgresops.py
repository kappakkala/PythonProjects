import os
import yaml
from datetime import datetime, timedelta
from dateutil.parser import parse
import psycopg2 as pg
import pandas as pd
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Postgresops:
    def __init__(self):
        # read db configuration from settings file
        self.read_settings()
        # creates a postgres connection
        self.create_connection()
        # get list of existing databases
        # self.list_databases(display=False)

    def read_settings(self):
        # gets the current active location of the file
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        # read settings
        with open(__location__ + "\settings.yaml") as f:
            self.settings = yaml.safe_load(f)

    def create_connection(self, dbname=None, display=True):
        # establish a postgres database connection using a client
        settings = self.settings
        try:
            if dbname == None:
                self.conn = pg.connect(
                    host=settings["host"],
                    user=settings["username"],
                    password=settings["password"],
                )
            else:
                self.conn = pg.connect(
                    host=settings["host"],
                    user=settings["username"],
                    password=settings["password"],
                    database=dbname,
                )
            # suppresses cannot run inside a transaction block error
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # create a cursor
            self.cur = self.conn.cursor()
            if display:
                if dbname == None:
                    print(f"Establishing connection to postgres databank.")
                else:
                    print(f"Establishing connection to postgres databank {dbname}.")
        except Exception:
            print("Error connecting to databank.")

    def list_databases(self, display=True):
        # lists all databases
        self.cur.execute("SELECT datname FROM pg_database;")
        # change tuple [('template1',), ('template0',)] to list
        self.list_db = [i[0] for i in self.cur.fetchall()]
        if display:
            print(self.list_db)

    def create_database(self, dbname):
        # creates a new database
        query = f"CREATE database {dbname};"
        try:
            self.cur.execute(query)
            print(f"Database {dbname} created successfully.")
        except Exception as e:
            print(f"No Database {dbname} is created : {e}")

    def create_schema(self, schema):
        query = f"CREATE SCHEMA IF NOT EXISTS {schema};"
        self.cur.execute(query)
        print(f"Schema {schema} created")

    def drop_schema(self, schema):
        query = f"DROP SCHEMA IF EXISTS {schema};"
        self.cur.execute(query)
        print(f"Schema {schema} deleted")

    def create_table(self, schema, tablename):
        # delete table if it already exists
        query = f"DROP TABLE IF EXISTS {schema}.{tablename}"
        self.cur.execute(query)
        # create a new table
        query = f"CREATE TABLE {schema}.{tablename}(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)"
        self.cur.execute(query)
        print(f"Table {tablename} created in schema {schema}")

    def insert_data_one(self, schema, tablename):
        # empty existing data from table
        self.empty_table(schema=schema, tablename=tablename) 
        # insert single data
        query = f"INSERT INTO {schema}.{tablename}(name, price) VALUES('Audi', 52642)"
        self.cur.execute(query)
        print(f"Inserted single data to table {schema}.{tablename}")

    def empty_table(self, schema, tablename):
        # to prevent duplicate insertion using the same id, we delete all data from table
        query = f"TRUNCATE {schema}.{tablename}"
        self.cur.execute(query)
        print(f"Emptied data from table {schema}.{tablename}")

    def insert_data_many(self, schema, tablename):
         # empty existing data from table
        self.empty_table(schema=schema, tablename=tablename) 
        # insert multiple data
        data = (
            (1, "Audi", 52642),
            (2, "Mercedes", 57127),
            (3, "Skoda", 9000),
            (4, "Volvo", 29000),
            (5, "Bentley", 350000),
            (6, "Citroen", 21000),
            (7, "Hummer", 41400),
            (8, "Volkswagen", 21600),
        )
        query = f"INSERT INTO {schema}.{tablename} (id, name, price) VALUES (%s, %s, %s)"
        self.cur.executemany(query, data)
        print(f"Inserted multiple data to table {schema}.{tablename}")

    def drop_table(self, schema, tablename):
        # delete table if it already exists
        query = f"DROP TABLE IF EXISTS {schema}.{tablename}"
        self.cur.execute(query)
        print(f"Table {tablename} deleted from schema {schema}")

    def drop_database(self, dbname):
        # disconnect the active database connection
        self.create_connection(display=False)
        # deletes an exisiting database
        query = f"DROP database {dbname};"
        try:
            self.cur.execute(query)
            print(f"Database {dbname} deleted successfully.")
        except Exception as e:
            print(f"No Database {dbname} is deleted : {e}")

    def close_connection(self):
        # closes the connection to postgres databank
        self.cur.close()
        self.conn.close()
        print("Database connection closed.")
