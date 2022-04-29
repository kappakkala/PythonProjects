import projectcars


def run_projectcars():
    # function to write mutiple data from a tuple into a generated table
    db = "testdb"
    schema = "testschema"
    tablename = "cars"
    # create a class object that creates a database and a table in a schema
    pypg = projectcars.Projectcars(dbname=db, schema=schema, tablename=tablename)
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
    run_projectcars()
