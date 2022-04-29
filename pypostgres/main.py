import projectcars

def run_projectcars():
    # function to write mutiple data from a tuple into a generated table
    db = "testdb"
    schema = "testschema"
    tablename = "cars"
    # create a class object that creates a database and a table in a schema
    pypg = projectcars.Projectcars(dbname=db, schema=schema, tablename=tablename)
    # get the most expensive car from the table
    pypg.print_most_expensive_car(schema=schema, tablename=tablename)
    # get all data in dataframe
    pypg.read_data_into_dataframe(schema=schema, tablename=tablename)
    # close database connection
    pypg.close_connection()


if __name__ == "__main__":
    run_projectcars()
