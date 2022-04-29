import pypostgresops


class Projectcars(pypostgresops.Postgresops):
    def __init__(self, dbname, schema, tablename):
        # run __init__ of parent class
        super().__init__()
        # prepare a project schema in a specified database
        self.prepare_schema(dbname=dbname, schema=schema)
        # create a new table
        self.create_table(schema=schema, tablename=tablename)

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
