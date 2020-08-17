from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time
import csv
from itertools import zip_longest
import json

with open('credentials.json') as f:
    config = json.load(f)

url, username, password, query = list(config['main'].values())    
driver = webdriver.PhantomJS()
#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options, executable_path = 'geckodriver.exe')

driver.get(url)
driver.find_element_by_id("loginData[email]").send_keys(username)
driver.find_element_by_id ("loginData[password]").send_keys(password)
driver.find_element_by_id("cbg3-submit-login").click()
driver.find_element_by_id("cbg3-submit").click()
driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div/div/div[3]/div[4]/a").click()
driver.find_element_by_id("search").send_keys(query)
driver.find_element_by_id("search").send_keys(Keys.RETURN)

connected = False
while not connected:
    try:
        driver.find_element_by_class_name("cbg3-offer-list-item--content").click()
        connected = True
    except NoSuchElementException:
        pass
driver.find_element_by_xpath("/html/body/section/div[2]/div/div[1]/div[1]/div/div[3]/div[2]/a/p").click()

driver.find_element_by_xpath("/html/body/section/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/button/span").click()

coupon_flag = False
while not coupon_flag:
    try:
        coupon = driver.find_element_by_xpath("/html/body/section/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[1]").text
        if coupon != "":
            coupon_flag = True
    except NoSuchElementException:
        pass
time.sleep(2)
#driver.save_screenshot('%s.png'%datetime.today().strftime("%Y-%m-%d"))
driver.find_element_by_xpath("/html/body/div[1]/header/div[4]/div/div[1]/div/a").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/header/div[4]/div/div[2]/nav/ul[3]/li/div[2]/a").click()
driver.quit()
f = open("codes.txt","a+")
f.write("%s %s \n" % (coupon, datetime.today().strftime("%Y-%m-%d")))
f.close()

list1 = ['%s'%datetime.today().strftime("%d-%m-%Y")]
list2 = ['%s'%coupon]
d = [list1, list2]
export_data = zip_longest(*d, fillvalue = '')
with open('codes.csv', 'a+', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerows(export_data)
myfile.close()
