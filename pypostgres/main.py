import projectcars
import json
import gc

def main():
    # run projectcars using psycopg2 library
    # pypg = projectcars.Carpsyco()
    # run projectcars using sqlalchemy library
    pypg = projectcars.Caralchemy()
    del pypg
    gc.collect()
    
if __name__ == "__main__":
    main()
