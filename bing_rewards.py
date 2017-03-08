"""Run Bing Searches Every Day"""

import os
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = os.getenv('MICROSOFT_USERNAME')
PASSWORD = os.getenv('MICROSOFT_PASSWORD')
ALLOWED_WEB_SEARCHES = 30
ALLOWED_MOBILE_SEARCHES = 20

def bing_search_web():
    web_searches = 0
    while web_searches < ALLOWED_WEB_SEARCHES:
        try:
            driver = webdriver.Chrome('./chromedriver')
            wait = WebDriverWait(driver, 10)

            driver.get('https://www.bing.com/')
            time.sleep(1)

            #sign in
            wait.until(EC.presence_of_element_located((By.ID, 'id_s')))
            driver.find_element_by_id('id_s').click()

            time.sleep(1)

            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'id_name')))
            driver.find_element_by_class_name('id_name').click()

            time.sleep(1)

            wait.until(EC.presence_of_element_located((By.ID, 'i0116')))
            wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
            driver.find_element_by_id('i0116').send_keys(USERNAME)
            driver.find_element_by_id('idSIButton9').click()

            time.sleep(1)

            wait.until(EC.presence_of_element_located((By.ID, 'i0118')))
            wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
            driver.find_element_by_id('i0118').send_keys(PASSWORD)
            driver.find_element_by_id('idSIButton9').click()

            time.sleep(1) #will redirect back to Bing

            num_searches_remaining = ALLOWED_WEB_SEARCHES - web_searches
            for i in xrange(num_searches_remaining):
                wait.until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
                driver.find_element_by_id('sb_form_q').clear()
                driver.find_element_by_id('sb_form_q').send_keys(generate_search(), Keys.RETURN)
                web_searches += 1
                time.sleep(5)
        except Exception:
            print "Caught exception. Continuing"
        finally:
            driver.close()

def bing_search_mobile():
    opts = Options()
    opts.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4')

    mobile_searches = 0
    while mobile_searches < ALLOWED_MOBILE_SEARCHES:
        try:
            driver = webdriver.Chrome('./chromedriver', chrome_options=opts)
            wait = WebDriverWait(driver, 10)

            driver.get('https://www.bing.com/')
            time.sleep(1)

            #sign in
            wait.until(EC.presence_of_element_located((By.ID, 'mHamburger')))
            driver.find_element_by_id('mHamburger').click()

            time.sleep(2) #needs to wait a bit longer here for DOM to update
            wait.until(EC.presence_of_element_located((By.ID, 'HBSignIn')))
            driver.find_element_by_id('HBSignIn').click()

            time.sleep(1)

            wait.until(EC.presence_of_element_located((By.ID, 'i0116')))
            wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
            driver.find_element_by_id('i0116').send_keys(USERNAME)
            driver.find_element_by_id('idSIButton9').click()

            time.sleep(1)

            wait.until(EC.presence_of_element_located((By.ID, 'i0118')))
            wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
            driver.find_element_by_id('i0118').send_keys(PASSWORD)
            driver.find_element_by_id('idSIButton9').click()

            time.sleep(1) #will redirect back to Bing

            num_searches_remaining = ALLOWED_MOBILE_SEARCHES - mobile_searches
            for i in xrange(num_searches_remaining):
                wait.until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
                driver.find_element_by_id('sb_form_q').clear()
                driver.find_element_by_id('sb_form_q').send_keys(generate_search(), Keys.RETURN)
                mobile_searches += 1
                time.sleep(5)
        except Exception:
            print "Caught exception. Continuing"
        finally:
            driver.close()

def generate_search():
    num_words = random.randint(1,5)
    search_string = ""
    for i in xrange(num_words):
        search_string += random.choice(words) + " "
    return search_string.strip()

with open('words.txt') as f:
    words = f.readlines()

bing_search_web()
bing_search_mobile()
