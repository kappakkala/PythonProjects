import pypostgresops

def main():
    # create a class object
    pypg = pypostgresops.Postgresops()
    # list all available databases
    pypg.list_databases()
    # create a new database
    db = 'testdb'
    pypg.create_database(dbname=db)   
    # delete an existing database
    pypg.drop_database(dbname=db) 
    # close database connection
    pypg.close_connection()

if __name__ == "__main__":
    main()