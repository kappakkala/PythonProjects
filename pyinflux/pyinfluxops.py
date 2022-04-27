import os
from influxdb import DataFrameClient
import yaml
from datetime import datetime, timedelta
from dateutil.parser import parse
import pandas as pd


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
        # get list of existing databases
        self.list_databases(display=False)
        # check if database already exists
        if database not in self.list_db:
            print(f"Database {database} does not exist. No database is deleted.")
        else:
            query = f"drop {database}"
            self.client.drop_database(database)
            print(f"Database {database} is deleted.")

    def list_measurements(self, db, display=True):
        # select the database
        self.client.switch_database(db)
        # list measurements
        list_measurements = self.client.get_list_measurements()
        if len(list_measurements)!=0:
            # list_measurements is a list of dicts with key 'name'
            self.list_measurements = [i["name"] for i in list_measurements]
        else:
            self.list_measurements = list_measurements
        if display:
            print(self.list_measurements)
    
    def write_data(self, db, df, measurement_write, influx_tags, influx_keys=None):
        # writes a pandas dataframe df into an influx measurement measurement_write using tags from dict influx_tags and list influx_keys
        # influx_tags is an identifier that is additional to df.columns 
        # influx_keys contains a list which is a subset of df.columns
        # select the database
        self.client.switch_database(db)
        # write data from df
        if len(df)!=0:
            if influx_keys == None:
                status = self.client.write_points(df, measurement_write, tags=influx_tags, protocol='line', batch_size=1000)
            else:
                status = self.client.write_points(df, measurement_write, tags=influx_tags, tag_columns=influx_keys, protocol='line', batch_size=1000)
        else:
            status = False
        
        if status:
            print(f"Data written succesfully in measurement {measurement_write} in database {db}.")
        else:
            print(f"No data is written. Check dataframe.")

    def close_connection(self):
        # closes the client connection
        self.client.close()
        print("Closing connection")

    def generate_test_dataframe(self):
        # initialize data of lists.
        data = {'name':['Tom', 'nick', 'krish', 'jack'],
                'age':[20, 21, 19, 18],
                'hobby': ['swimming', 'football', 'fencing', 'swimming']}
        self.df = pd.DataFrame(data=data)
        self.df.index = [parse('2022-01-13 17:00:00')+timedelta(minutes=i) for i in range(len(self.df))]

    def read_data(self, db, measurement_read, query=None):
        # reads the available data from measurement based on a query
        if query == None:
            query = f"select * from {measurement_read}"
        df = self.client.query(query=query, database=db, data_frame_index='time')
        if not df =={}:
            df = pd.concat(df, axis = 1)
            df.columns = df.columns.droplevel()
            df.index = pd.to_datetime(df.index, format='%Y%m%d %H:%M:%S').tz_localize(None)
        else:
            df = pd.DataFrame()
            print('No data is available. Check query and measurements')
        return df