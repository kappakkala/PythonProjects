from time import sleep
import subprocess
import automate
import pyautogui as pg
from screeninfo import get_monitors

def main():
    pyauto = automate.Automate()
    #subprocess.Popen(pyauto.settings['program'])
    pg.moveTo(220, 1050, 0.2)        
    pg.click(220,1050)
    sleep(1)
    # get coordinates of load button
    loc_load = list(pg.locateAllOnScreen(pyauto.image_dir+'load.png'))[0]
    offset = 10
    x_load, y_load = loc_load.left+offset, loc_load.top+offset
    pg.moveTo(x_load, y_load, 0.2)
    pg.click(x_load, y_load)
    sleep(2)
    pyauto.connect_jump()

if __name__ == "__main__":
    main()


