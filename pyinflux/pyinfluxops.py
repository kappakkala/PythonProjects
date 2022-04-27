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
        

    def read_settings(self):
        # gets the current active location of the file
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        # read settings
        with open(__location__+'\settings.yaml') as f:
            self.settings = yaml.safe_load(f)

    def create_connection(self):
        # establish an influx database connection using a client
        settings = self.settings
        self.client = DataFrameClient(host=settings['host'], port=settings['port'], username=settings['username'], password=settings['password'])
        print('Establishing connection to influx databank')

    
    def show_databases(self):
        # get list of databases
        list_db = self.client.get_list_database()
        # list_db is a list of dicts with key 'name'
        list_db = [i['name'] for i in list_db]
        print('Database contains ')
        print(list_db)
    
    def close_connection(self):
        # closes the client connection
        self.client.close()
        print('Closing connection')