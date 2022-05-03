import os
import yaml
from time import sleep
import pyautogui as pg


class Automate:
    def __init__(self):
        # read db configuration from settings file
        self.read_settings()
        
    def read_settings(self):
        # gets the current active location of the file
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        # read settings
        with open(__location__ + "\settings.yaml") as f:
            self.settings = yaml.safe_load(f)
        # get image directory
        self.image_dir = __location__ + "\images\\"

    def connect_jump(self):
        pg.typewrite(self.settings['jump_settings'])
        pg.hotkey('enter')
        sleep(1)
        pg.hotkey('enter')
        sleep(3)
        pg.typewrite(self.settings['jump_user'])
        pg.hotkey('tab')
        sleep(1)
        pg.typewrite(self.settings['jump_password'])
        pg.hotkey('enter')