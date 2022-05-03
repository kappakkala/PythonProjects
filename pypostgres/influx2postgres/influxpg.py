from influxdb import DataFrameClient
import pandas as pd
import pypostgresops
from influx2postgres import db_name, schema_name, table_name


class Influxpg(pypostgresops.Alchemy):
    def __init__(self, settings):
        self.influx_settings = settings["influx"]
        # run __init__ of parent class
        self.pg_settings = settings["postgres"]
        super().__init__(settings=self.pg_settings)

        self.create_influx_connection()
        # save data from influx measurement into a dataframe
        self.df = self.read_data(
            db_name=settings["influx"]["db"],
            measurement_read=settings["influx"]["measurement_read"],
        )
        # prepare a project schema in a specified database
        self.prepare_schema(db_name=db_name, schema_name=schema_name)
        # create a postgres table from df data
        self.create_table(schema_name=schema_name, table_name=table_name)

    def create_influx_connection(self):
        # establish an influx database connection using a client
        settings = self.influx_settings
        self.client = DataFrameClient(
            host=settings["host"],
            port=settings["port"],
            username=settings["username"],
            password=settings["password"],
        )
        print("Establishing connection to influx databank")

    def read_data(self, db_name, measurement_read, query=None):
        # reads the available data from measurement based on a query
        # select the database
        self.client.switch_database(db_name)
        if query is None:
            query = f"select * from {measurement_read}"
        df = self.client.query(query=query, database=db_name, data_frame_index="time")
        if not df == {}:
            df = pd.concat(df, axis=1)
            df.columns = df.columns.droplevel()
            df.index = pd.to_datetime(df.index, format="%Y%m%d %H:%M:%S").tz_localize(
                None
            )
        else:
            df = pd.DataFrame()
            print("No data is available. Check query and measurements")
        return df

    def create_table(self, schema_name, table_name):
        # creates a new table from pandas dataframe
        try:
            result = self.df.to_sql(
                name=table_name,
                con=self.engine,
                schema=schema_name,
                if_exists="replace",
            )
            print(f"{result} rows affected in table {schema_name}.{table_name}")
        except Exception as e:
            print(f"Error writing dataframe to table : {e}")
