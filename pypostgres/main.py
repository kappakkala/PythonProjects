import pypostgresops

def main():
    # create a class object
    pypg = pypostgresops.Postgresops()
    # execute a statement
    print('PostgreSQL database version:')
    pypg.cur.execute('SELECT version()')
    # display the PostgreSQL database server version
    db_version = pypg.cur.fetchone()
    print(db_version)
    # close database connection
    pypg.close_connection()

if __name__ == "__main__":
    main()