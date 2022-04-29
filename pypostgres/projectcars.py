import pypostgresops

class Projectcars(pypostgresops.Postgresops):
    
    def __init__(self):
        # run __init__ of parent class
        super().__init__()
        # create a new database
        db = 'testdb'
        schema = 'testschema'
        tablename = 'cars'
        self.create_database(dbname=db)
        # connect to the database
        self.create_connection(dbname=db)
        # create a schema
        self.create_schema(schema=schema)
        # create a new table
        self.create_table(schema=schema, tablename=tablename)
        # insert a single data
        self.insert_data_one(schema=schema, tablename=tablename)
        # insert multiple data
        self.insert_data_many(schema=schema, tablename=tablename)
        # delete an existing table
        # self.drop_table(schema=schema, tablename=tablename)
        # delete a schema
        # self.drop_schema(schema=schema)
        # delete an existing database
        # self.drop_database(dbname=db)

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