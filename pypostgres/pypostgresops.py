import psycopg2 as pg
import pandas as pd
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, schema


class Psyco(object):
    def __init__(self, settings):
        self.pg_settings = settings
        # creates a postgres connection
        self.create_connection()
        # get list of existing databases
        self.list_databases(display=True)

    def create_connection(self, db_name=None, display=True):
        # establish a postgres database connection using a client
        pg_settings = self.pg_settings
        try:
            if db_name is None:
                self.conn = pg.connect(
                    host=pg_settings["host"],
                    user=pg_settings["username"],
                    password=pg_settings["password"],
                )
            else:
                self.conn = pg.connect(
                    host=pg_settings["host"],
                    user=pg_settings["username"],
                    password=pg_settings["password"],
                    database=db_name,
                )
            # suppresses cannot run inside a transaction block error
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # create a cursor
            self.cur = self.conn.cursor()
            if display:
                if db_name is None:
                    print("Establishing connection to postgres databank.")
                else:
                    print(f"Establishing connection to postgres databank {db_name}.")
        except Exception:
            print("Error connecting to databank.")

    def list_databases(self, display=True):
        # lists all databases
        self.cur.execute("SELECT datname FROM pg_database;")
        # change tuple [('template1',), ('template0',)] to list
        self.list_db = [i[0] for i in self.cur.fetchall()]
        if display:
            print(self.list_db)

    def create_database(self, db_name):
        # creates a new database
        query = f"CREATE database {db_name};"
        try:
            self.cur.execute(query)
            print(f"Database {db_name} created successfully.")
        except Exception as e:
            print(f"No Database {db_name} is created : {e}")

    def create_schema(self, schema_name):
        query = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
        self.cur.execute(query)
        print(f"Schema {schema_name} is created")

    def prepare_schema(self, db_name, schema_name):
        # prepare a project schema in a specified database
        # create a new database
        self.create_database(db_name=db_name)
        # connect to the database
        self.create_connection(db_name=db_name)
        # create a schema
        self.create_schema(schema_name=schema_name)

    def drop_schema(self, schema_name):
        # drops an existing schema from the database
        query = f"DROP SCHEMA IF EXISTS {schema_name};"
        self.cur.execute(query)
        print(f"Schema {schema_name} is deleted")

    def empty_table(self, schema_name, table_name):
        # to prevent duplicate insertion using the same id, we delete all data from table
        query = f"TRUNCATE {schema_name}.{table_name}"
        self.cur.execute(query)
        print(f"Emptied data from table {schema_name}.{table_name}")

    def drop_table(self, schema_name, table_name):
        # delete table if it already exists
        query = f"DROP TABLE IF EXISTS {schema_name}.{table_name}"
        self.cur.execute(query)
        print(f"Table {table_name} deleted from schema {schema_name}")

    def drop_database(self, db_name):
        # disconnect the active database connection
        self.create_connection(display=False)
        # deletes an exisiting database
        query = f"DROP database {db_name};"
        try:
            self.cur.execute(query)
            print(f"Database {db_name} deleted successfully.")
        except Exception as e:
            print(f"No Database {db_name} is deleted : {e}")

    def close_connection(self):
        # closes the connection to postgres databank
        self.cur.close()
        self.conn.close()
        print("Database connection closed.")

    def read_data_into_dataframe(self, schema_name, table_name):
        # get all the data from the table
        query = f"""SELECT * FROM {schema_name}."{table_name}";"""
        df = pd.read_sql_query(query, self.conn, index_col=None, parse_dates=None)
        return df


class Alchemy(object):
    def __init__(self, settings):
        self.pg_settings = settings
        # establish database connection
        self.create_connection()
        # get list of existing databases
        self.list_databases(display=True)

    def create_connection(self, db_name=None, display=True):
        try:
            if db_name is None:
                url = URL.create(**self.pg_settings)
            else:
                self.pg_settings["database"] = db_name
                url = URL.create(**self.pg_settings)
            # start engine
            self.engine = create_engine(url)
            # connect engine
            self.conn = self.engine.connect()
            # set isolation/commit
            self.conn.execute("commit")
            if display:
                if db_name is None:
                    print("Establishing connection to postgres databank.")
                else:
                    print(f"Establishing connection to postgres databank {db_name}.")
        except Exception as e:
            print(f"Could not establish connection : {e}")

    def list_databases(self, display=True):
        # lists all databases
        list_db = self.engine.execute("SELECT datname FROM pg_database;").fetchall()
        # change tuple [('template1',), ('template0',)] to list
        self.list_db = [i[0] for i in list_db]
        if display:
            print(self.list_db)

    def create_database(self, db_name):
        # creates a new database
        query = f"CREATE database {db_name};"
        try:
            self.conn.execute(query)
            print(f"Database {db_name} created successfully.")
        except Exception as e:
            print(f"No Database {db_name} is created : {e}")

    def create_schema(self, schema_name):
        # create a new schema if it doesn't exist
        if not self.engine.dialect.has_schema(self.engine, schema_name):
            self.engine.execute(schema.CreateSchema(schema_name))
            print(f"Schema {schema_name} is created")

    def drop_schema(self, schema_name):
        # delete an already existing schema
        if self.engine.dialect.has_schema(self.engine, schema_name):
            self.engine.execute(schema.DropSchema(schema_name, cascade=True))
            print(f"Schema {schema_name} is deleted")

    def prepare_schema(self, db_name, schema_name):
        # prepare a project schema in a specified database
        # create a new database
        self.create_database(db_name=db_name)
        # connect to the database
        self.create_connection(db_name=db_name)
        # create a schema
        self.create_schema(schema_name=schema_name)

    def empty_table(self, schema_name, table_name):
        # to prevent duplicate insertion using the same id, we delete all data from table
        query = f"TRUNCATE {schema_name}.{table_name}"
        self.conn.execute(query)
        print(f"Emptied data from table {schema_name}.{table_name}")

    def drop_database(self, db_name):
        """
        Issues : (psycopg2.errors.ObjectInUse) cannot drop the currently open database
        """
        # disconnect the active database connection
        self.create_connection(display=False)
        # deletes an exisiting database
        query = f"DROP database {db_name} WITH (FORCE);"
        try:
            self.conn.execute(query)
            print(f"Database {db_name} deleted successfully.")
        except Exception as e:
            print(f"No Database {db_name} is deleted : {e}")

    def close_connection(self):
        self.conn.close()
        print("Database connection closed.")

    def read_data_into_dataframe(self, schema_name, table_name):
        # get all the data from the table
        query = f"""SELECT * FROM {schema_name}."{table_name}";"""
        try:
            df = pd.read_sql_query(query, self.conn, index_col='time', parse_dates=None)
        # if 'time' column is not present
        except KeyError:
            df = pd.read_sql_query(query, self.conn, index_col=None, parse_dates=None)
        return df
