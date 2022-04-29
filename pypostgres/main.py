import pypostgresops

def main():
    # create a class object
    pypg = pypostgresops.Postgresops()
    # list all available databases
    pypg.list_databases()
    # create a new database
    db = 'testdb'
    # pypg.create_database(dbname=db)
    # connect to the database
    pypg.create_connection(dbname=db)
    # create a schema
    schema = 'testschema'
    pypg.create_schema(schema=schema)
    # create a new table
    tablename = 'cars'
    pypg.create_table(schema=schema, tablename=tablename)
    # insert a single data
    # pypg.insert_data_one(schema=schema, tablename=tablename)
    # insert multiple data
    pypg.insert_data_many(schema=schema, tablename=tablename)
    # delete an existing table
    # pypg.drop_table(schema=schema, tablename=tablename)
    # delete a schema
    # pypg.drop_schema(schema=schema)
    # delete an existing database
    # pypg.drop_database(dbname=db) 
    # close database connection
    pypg.close_connection()

if __name__ == "__main__":
    main()