from projectcars import pypsycopg, pysqlalchemy
import json
import gc

def main():
    # run projectcars using psycopg2 library
    pypg = pypsycopg.Carpsyco()
    # run projectcars using sqlalchemy library
    # pypg = pysqlalchemy.Caralchemy()
    del pypg
    gc.collect()


if __name__ == "__main__":
    main()
