import pyinfluxops
import pandas as pd
def main():
    # create a class object
    pyflux = pyinfluxops.Influxops()
    db = 'test'
    # lists exisiting databases
    pyflux.list_databases()
    # create a new database
    pyflux.create_database(db)
    # lists exisiting measurements from database
    pyflux.list_measurements(db)
    # generates a test timeseries dataframe with name, age, hobby columns
    pyflux.generate_test_dataframe()
    # write df to influx
    pyflux.write_data(db=db, df=pyflux.df, measurement_write='test_measurement', influx_tags={'testfield':'type1'}, influx_keys = ['hobby'])
    # read data from measurement based on query and store the results to a df
    measurement_read = "test_measurement"
    df = pyflux.read_data(db=db, measurement_read=measurement_read, query=None)
    print(df)
    # delete a database
    pyflux.drop_database(db)
    # close connection
    pyflux.close_connection()


if __name__ == "__main__":
    main()
