'''
Issues:

Multi-language Dropboxes
Multiple PDFs at link
Dropbox 404 Pages
'''

import os, time, urllib
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

filepath = '/media/jon-moreno/Backup Data/Dropbox (Library for All)/ASb/BookDash/'
start = 73 #default is 2
stop = 84

def download(elem):
    #Creates DL URL
    url = elem.get_attribute("href").rstrip("0")+"1"
    
    #Creates filename from URL
    filename = urlparse(url).path.split('/')[-1]

    #Performs download
    urllib.request.urlretrieve(url, filepath+filename)

driver = webdriver.Chrome()
driver.get("http://bookdash.org/see/books/")
parent_window = driver.window_handles[0]

for i in range(start, stop):
    #Finds ea. link on BookDash
    xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[{}]/a[3]'.format(i)
    elem = driver.find_element_by_xpath(xpath)

    #Performs direct dl where available
    if (elem.get_attribute("href").endswith(".pdf?dl=0")):
        download(elem)
        continue

    #Opens new tab & switches to it
    elem.send_keys(Keys.CONTROL,Keys.RETURN)
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5) #Delay for loading

    css = '.sl-link--file' #Represents the CSS selector of a-tag w. dl url
    elem = driver.find_element_by_css_selector(css)
    download(elem)
    driver.close()
    driver.switch_to_window(parent_window)

driver.quit()