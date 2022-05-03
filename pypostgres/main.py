# from projectcars import pypsycopg, pysqlalchemy
from influx2postgres import influxpg
from settings import settings
import gc


def main():
    # run projectcars using psycopg2 library
    # pypg = pypsycopg.Carpsyco(settings["postgres"])
    # run projectcars using sqlalchemy library
    # pypg = pysqlalchemy.Caralchemy(settings["postgres"])
    # read from influx measurement as dataframe and save it to postgres table
    pypg = influxpg.Influxpg(settings)
    del pypg
    gc.collect()


if __name__ == "__main__":
    main()
