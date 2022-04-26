import os
from influxdb import DataFrameClient
import yaml
import pandas

def main():
    # gets the current active location of the file
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    # read settings
    with open(__location__+'\settings.yaml') as f:
        settings = yaml.safe_load(f)

    # establish an influx database connection using a client
    client = DataFrameClient(host=settings['host'], port=settings['port'], username=settings['username'], password=settings['password'])

    # get list of databases
    list_db = client.get_list_database()
    # list_db is a list of dicts with key 'name'
    list_db = [i['name'] for i in list_db]
    print(list_db)

    # close connection
    client.close()

if __name__ == "__main__":
    main()
