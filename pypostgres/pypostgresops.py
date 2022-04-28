import os
import yaml
from datetime import datetime, timedelta
from dateutil.parser import parse
import psycopg2 as pg
import pandas as pd


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

    def create_connection(self):
        # establish a postgres database connection using a client
        settings = self.settings
        try:
            self.conn = pg.connect(
                host=settings["host"],
                user=settings["username"],
                password=settings["password"],
            )
            # create a cursor
            self.cur = self.conn.cursor()
            print("Establishing connection to postgres databank.")
        except Exception:
            print("Error connecting to databank.")

    def list_databases(self, display=True):
        # lists all databases
        self.cur.execute('SELECT datname FROM pg_database;')
        # change tuple [('template1',), ('template0',)] to list
        self.list_db = [i[0] for i in self.cur.fetchall()]
        if display:
            print(self.list_db)

    def close_connection(self):
        # closes the connection to postgres databank
        self.cur.close()
        self.conn.close()
        print('Database connection closed.')