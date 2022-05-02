import projectcars
import json

def run_carspsyco():
    # function to write mutiple data from a tuple into a generated table
    db_name = "testdb"
    schema_name = "testschema"
    table_name = "cars"
    # create a class object that creates a database and a table in a schema
    pypg = projectcars.Carpsyco(db_name=db_name, schema_name=schema_name, table_name=table_name)
    # get the most expensive car from the table
    pypg.print_most_expensive_car(schema_name=schema_name, table_name=table_name)
    # get all data in dataframe
    # df = pypg.read_data_into_dataframe(schema_name=schema_name, table_name=table_name)
    # close database connection
    pypg.close_connection()

def run_carsalchemy():
    db_name = "testdb"
    schema_name = "testschema"
    table_name = "cars"
     # create a class object that creates a database and a table in a schema
    pypg = projectcars.Caralchemy(db_name=db_name, schema_name=schema_name, table_name=table_name)
    # get the most expensive car from the table
    pypg.print_most_expensive_car(schema_name=schema_name, table_name=table_name)
    # get all data in dataframe
    # df = pypg.read_data_into_dataframe(schema_name=schema_name, table_name=table_name)
    # close database connection
    pypg.close_connection()

if __name__ == "__main__":
    # execute project using psycopg2
    # run_carspsyco()
    # execute project using sqlalchemy
    run_carsalchemy()
