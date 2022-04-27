import pyinfluxops


def main():
    # create a class object
    pyflux = pyinfluxops.Influxops()
    # create a new database
    pyflux.create_database("test")
    # delete a database
    pyflux.drop_database("test")
    # close connection
    pyflux.close_connection()


if __name__ == "__main__":
    main()
