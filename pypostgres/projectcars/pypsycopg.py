import pypostgresops
import pandas as pd
from Projectcars import db_name, schema_name, table_name


class Carpsyco(pypostgresops.Psyco):
    def __init__(self):
        # run __init__ of parent class
        super().__init__()
        # prepare a project schema in a specified database
        self.prepare_schema(db_name=db_name, schema_name=schema_name)
        # create a new table
        self.create_table(schema_name=schema_name, table_name=table_name)
        # insert a single data
        # self.insert_data_one(schema_name=schema_name, table_name=table_name)
        # insert multiple data
        self.insert_data_many(schema_name=schema_name, table_name=table_name)
        # get the most expensive car from the table
        self.print_most_expensive_car(schema_name=schema_name, table_name=table_name)
        # get all data in dataframe
        df = self.read_data_into_dataframe(schema_name=schema_name, table_name=table_name)
        print(df)
        # delete an existing table
        # self.drop_table(schema_name=schema_name, table_name=table_name)
        # delete a schema
        # self.drop_schema(schema_name=schema_name)
        # delete an existing database
        # self.drop_database(db_name=db_name)
        # close database connection
        self.close_connection()

    def create_table(self, schema_name, table_name):
        # delete table if it already exists
        query = f"DROP TABLE IF EXISTS {schema_name}.{table_name}"
        self.cur.execute(query)
        # create a new table
        try:
            query = f"CREATE TABLE {schema_name}.{table_name}(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)"
            self.cur.execute(query)
            print(f"Table {table_name} created in schema {schema_name}")
        except:
            pass

    def insert_data_one(self, schema_name, table_name):
        # empty existing data from table
        self.empty_table(schema_name=schema_name, table_name=table_name)
        # insert single data
        query = f"INSERT INTO {schema_name}.{table_name}(name, price) VALUES('Audi', 52642)"
        self.cur.execute(query)
        print(f"Inserted single data to table {schema_name}.{table_name}")

    def insert_data_many(self, schema_name, table_name):
        # empty existing data from table
        self.empty_table(schema_name=schema_name, table_name=table_name)
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
        query = (
            f"INSERT INTO {schema_name}.{table_name} (id, name, price) VALUES (%s, %s, %s)"
        )
        self.cur.executemany(query, data)
        print(f"Inserted multiple data to table {schema_name}.{table_name}")

    def print_most_expensive_car(self, schema_name, table_name):
        # prints the most expensive car from the table
        query = f"SELECT name from {schema_name}.{table_name} where price = (SELECT MAX(price) from {schema_name}.{table_name});"
        self.cur.execute(query)
        car = self.cur.fetchall()
        # get the string value 'car' from list [('car'),]
        print(car[0][0])