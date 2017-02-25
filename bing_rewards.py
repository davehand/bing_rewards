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

def bing_search_web(words):
    driver = webdriver.Chrome('./chromedriver')
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.bing.com/')
    time.sleep(1)

    #sign in
    wait.until(EC.presence_of_element_located((By.ID, 'id_s')))
    driver.find_element_by_id('id_s').click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'id_name')))
    driver.find_element_by_class_name('id_name').click()

    wait.until(EC.presence_of_element_located((By.ID, 'i0116')))
    wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
    driver.find_element_by_id('i0116').send_keys(USERNAME)
    driver.find_element_by_id('idSIButton9').click()

    wait.until(EC.presence_of_element_located((By.ID, 'i0118')))
    wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
    driver.find_element_by_id('i0118').send_keys(PASSWORD)
    driver.find_element_by_id('idSIButton9').click()

    time.sleep(1) #will redirect back to Bing

    for i in xrange(30):
        wait.until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
        driver.find_element_by_id('sb_form_q').clear()
        driver.find_element_by_id('sb_form_q').send_keys(random.choice(words), Keys.RETURN)
        time.sleep(5)

    driver.close()


def bing_search_mobile(words):
    opts = Options()
    opts.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4')

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

    wait.until(EC.presence_of_element_located((By.ID, 'i0116')))
    wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
    driver.find_element_by_id('i0116').send_keys(USERNAME)
    driver.find_element_by_id('idSIButton9').click()

    wait.until(EC.presence_of_element_located((By.ID, 'i0118')))
    wait.until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
    driver.find_element_by_id('i0118').send_keys(PASSWORD)
    driver.find_element_by_id('idSIButton9').click()

    time.sleep(1) #will redirect back to Bing

    for i in xrange(20):
        wait.until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
        driver.find_element_by_id('sb_form_q').clear()
        driver.find_element_by_id('sb_form_q').send_keys(random.choice(words), Keys.RETURN)
        time.sleep(5)

    driver.close()


with open('words.txt') as f:
    words = f.readlines()

bing_search_web(words)
bing_search_mobile(words)
