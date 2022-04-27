import os
from influxdb import DataFrameClient
import yaml
import pandas


class Influxops:
    def __init__(self):
        # read db configuration from settings file
        self.read_settings()
        # creates an influx client
        self.create_connection()
        # get list of existing databases
        self.list_databases(display=False)

    def read_settings(self):
        # gets the current active location of the file
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        # read settings
        with open(__location__ + "\settings.yaml") as f:
            self.settings = yaml.safe_load(f)

    def create_connection(self):
        # establish an influx database connection using a client
        settings = self.settings
        self.client = DataFrameClient(
            host=settings["host"],
            port=settings["port"],
            username=settings["username"],
            password=settings["password"],
        )
        print("Establishing connection to influx databank")

    def list_databases(self, display=True):
        # get list of databases
        list_db = self.client.get_list_database()
        # list_db is a list of dicts with key 'name'
        self.list_db = [i["name"] for i in list_db]
        if display:
            print(self.list_db)

    def create_database(self, database):
        # check if database already exists
        if database in self.list_db:
            print(f"Database {database} already exists. No new database is created.")
        else:
            self.client.create_database(database)
            print(f"Database {database} is created.")

    def drop_database(self, database):
        # check if database already exists
        if database not in self.list_db:
            print(f"Database {database} does not exist. No database is deleted.")
        else:
            query = f"drop {database}"
            self.client.drop_database(database)
            print(f"Database {database} is deleted.")

    def close_connection(self):
        # closes the client connection
        self.client.close()
        print("Closing connection")
