import pypostgresops
import pandas as pd

class Projectcars(pypostgresops.Postgresops):
    def __init__(self, dbname, schema, tablename):
        # run __init__ of parent class
        super().__init__()
        # prepare a project schema in a specified database
        self.prepare_schema(dbname=dbname, schema=schema)
        # create a new table
        self.create_table(schema=schema, tablename=tablename)
        # insert a single data
        # self.insert_data_one(schema=schema, tablename=tablename)
        # insert multiple data
        self.insert_data_many(schema=schema, tablename=tablename)
        # delete an existing table
        # self.drop_table(schema=schema, tablename=tablename)
        # delete a schema
        # self.drop_schema(schema=schema)
        # delete an existing database
        # self.drop_database(dbname=db)

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

    def print_most_expensive_car(self, schema, tablename):
        # prints the most expensive car from the table
        query = f"SELECT name from {schema}.{tablename} where price = (SELECT MAX(price) from {schema}.{tablename});"
        self.cur.execute(query)
        car = self.cur.fetchall()  
        # get the string value 'car' from list [('car'),]
        print(car[0][0])
    
    def read_data_into_dataframe(self, schema, tablename):
        # get all the data from the table
        query = f"SELECT * FROM {schema}.{tablename}"
        df = pd.read_sql_query(query, self.conn, index_col=None, parse_dates=None)
        print(df)