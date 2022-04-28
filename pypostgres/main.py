import pypostgresops

def main():
    # create a class object
    pypg = pypostgresops.Postgresops()
    # list all available databases
    pypg.list_databases()    
    # close database connection
    pypg.close_connection()

if __name__ == "__main__":
    main()