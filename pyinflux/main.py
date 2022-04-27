import pyinfluxops

def main():    
    # create a class object
    pyflux = pyinfluxops.Influxops()
    # displays the exisiting databases
    pyflux.show_databases()
    # close connection
    pyflux.close_connection()

if __name__ == "__main__":
    main()
