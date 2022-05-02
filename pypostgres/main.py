from projectcars import pypsycopg, pysqlalchemy
from settings import settings
import gc

def main():
    # run projectcars using psycopg2 library
    # pypg = pypsycopg.Carpsyco(settings["postgres"])
    # run projectcars using sqlalchemy library
    pypg = pysqlalchemy.Caralchemy(settings["postgres"])

    # pypg = influxpg.Influxpg(settings["influx"]) 
    del pypg
    gc.collect()


if __name__ == "__main__":
    main()
