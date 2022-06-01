import os
import yaml
from sqlalchemy import text # for reading .sql files 

class Settings:
    def __init__(self):
        # gets the current active location of the file
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        # read settings
        with open(__location__ + "\settings.yaml") as f:
            self.settings = yaml.safe_load(f)

        # read sql file
        with open(__location__ + "\\test.sql") as file:
            self.sql_file_query = text(file.read())