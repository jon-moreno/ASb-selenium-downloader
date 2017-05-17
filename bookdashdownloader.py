import os, time, urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Opens FF to webpage using existing profile
profile = webdriver.FirefoxProfile('/home/jon-moreno/.mozilla/firefox/c7r83610.temp')
driver = webdriver.Firefox(profile)
driver.get("http://bookdash.org/see/books/")
parent_window = driver.window_handles[0]
child_window = 0

for i in range(2, 84):
    xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[{}]/a[3]'.format(i)
    elem = driver.find_element_by_xpath(xpath)
    elem.send_keys(Keys.CONTROL,Keys.RETURN)

    child_window = driver.window_handles[1]
    driver.switch_to.window(child_window)
    time.sleep(5)

    #css = 'css=a.sl-link.sl-link--file > div.sl-grid-filename'
    #css = '.sl-link--file > div:nth-child(2)'
    css = '.sl-link--file'
    elem = driver.find_element_by_css_selector(css)
    
    url = elem.get_attribute("href")
    url = url.rstrip("0")
    url = url+"1"
    
    #urllib.request.urlopen()

    driver.get(url)
    driver.close()
    driver.switch_to().window(parent_window)

driver.quit()