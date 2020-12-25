#created by Alex v Ajith
##  Execute script and let the computer attend your class on its own...Have Fun!😉 ##
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime 
import calendar
from datetime import date

#meet links
oops = 'https://meet.google.com/lookup/b4rypbzbty'
data_str = 'https://meet.google.com/lookup/ccxz22fj2o'
design = 'https://meet.google.com/lookup/hx3bvkaomg'
maths ='https://meet.google.com/lookup/hjkyavbdjo'
logic ='https://meet.google.com/lookup/dzvqp2wfsv'
sus = 'https://meet.google.com/lookup/adgxkdphjm'
#time tables
today = date.today().strftime('%Y %m %d')
dayno = datetime.datetime.strptime(today, '%Y %m %d').weekday() 
day = (calendar.day_name[dayno])
print(day)
Monday = [data_str,design,maths,oops]
Tuesday = [maths,oops,logic,design]
Wednesday = [logic,maths,oops,data_str]
Thursday = [oops,data_str,logic,sus]
Friday = [sus,maths,data_str,logic]

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--lang=en-us")
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")
driver = webdriver.Chrome()
driver.get('https://classroom.google.com/u/1/h')
time.sleep(1) # Let the user actually see something!
# driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
login_text = driver.find_element_by_xpath('//*[@id="identifierId"]')
login_text.send_keys(email_id)
driver.find_element_by_id("identifierNext").click()
time.sleep(3)
pwd = driver.find_element_by_xpath('//*[@class="whsOnd zHQkBf"]').send_keys(your_password)
driver.find_element_by_id('passwordNext').click()
time.sleep(3)

#entering classes
if (day == 'Monday'):
    for classes in Monday:
        driver.get(classes)
        time.sleep(6)
        #delete popups
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath('//*[@class="NPEfkd RveJvd snByac"]').click()
        #Enter time required for each class
        classstime = 30
        time.sleep(classstime) # Let the user actually see something!
        driver.find_element_by_xpath('//*[@class="U26fgb JRY2Pb mUbCce kpROve GaONte Qwoy0d ZPasfd vzpHY"]').click()
        print(time.time)
elif(day == 'Tuesday'):
    for classes in Tuesday:
        driver.get(classes)
        time.sleep(6)
        #delete popups
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath('//*[@class="NPEfkd RveJvd snByac"]').click()
        #Enter time required for each class
        classstime = 30
        time.sleep(classstime) # Let the user actually see something!
        driver.find_element_by_xpath('//*[@class="U26fgb JRY2Pb mUbCce kpROve GaONte Qwoy0d ZPasfd vzpHY"]').click()
        print(time.time)
elif(day == 'Wednesday'):
    for classes in Wednesday:
        driver.get(classes)
        time.sleep(6)
        #delete popups
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath('//*[@class="NPEfkd RveJvd snByac"]').click()
        #Enter time required for each class
        classstime = 30
        time.sleep(classstime) # Let the user actually see something!
        driver.find_element_by_xpath('//*[@class="U26fgb JRY2Pb mUbCce kpROve GaONte Qwoy0d ZPasfd vzpHY"]').click()
        print(time.time)
elif(day == 'Thursday'):
    for classes in Thursday:
        driver.get(classes)
        time.sleep(6)
        #delete popups
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath('//*[@class="NPEfkd RveJvd snByac"]').click()
        #Enter time required for each class
        classstime = 30
        time.sleep(classstime) # Let the user actually see something!
        driver.find_element_by_xpath('//*[@class="U26fgb JRY2Pb mUbCce kpROve GaONte Qwoy0d ZPasfd vzpHY"]').click()
        print(time.time)
elif(day == 'Friday'):
    for classes in Friday:
        driver.get(classes)
        time.sleep(6)
        #delete popups
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath('//*[@class="NPEfkd RveJvd snByac"]').click()
        #Enter time required for each class
        classstime = 30
        time.sleep(8)
        #Also wanted to implement a 'Good morning miss' Genertor
        time.sleep(classstime) # Let the user actually see something!
        driver.find_element_by_xpath('//*[@class="U26fgb JRY2Pb mUbCce kpROve GaONte Qwoy0d ZPasfd vzpHY"]').click()
        print(time.time)
driver.quit()
