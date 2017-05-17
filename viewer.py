import os
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

books = [
###LEVEL 1###
#"A very tall man",
#"Colours of a rainbow",
#"Frog and Snake",
#"Friends",
#"How tortoise got a crooked nose",
#"Hyena, Hare and basins",
#"Lazy Anansi", #
#"Monkey and the drought",
#"Palm tree",
#"Porridge",
#"Which work is the most important?",
#"Chicken and Millipede", #
###LEVEL 2###
#"Africa Unity Race",
#"Azizi the doll",
#"Big blue bus", #
#"Curious Baby Elephant", #
#"Death visits Hupapa",
#"Fire's story",
#"Goat, Dog and Cow", #
#"Hamisi's lucky day",
#"Jaaka the fisherman",
#"My family and I",
#"Ostrich and Lioness",
#"Selemeng's cats",
#"The day the sun went away",
#"Two little friends",
#"Two thieves",
#"Why Ajao was not buried",
#"Wind", #
###LEVEL 3###
#"Adun, the beautiful",
#"Beloved daughter", #
#"Byantaka and the dead pot",
#"Creature with two",
#"Crushed louse",
#"Fox and Rooster",
#"Goat and Hyena's knife",
#"Holidays with grandmother",
#"Hyena and Tortoise", #
#"Kalabushe the talkative",
#"Maguru gives legs",
#"Pontshibobo's tree",
#"The girl who got rich",
#"Thunder and Lightning",
###LEVEL 4###
"Counting cabbages", #
"Hare and Hyena", #
"King Kayanja and his daughter",
"Magozwe", #
"Share it fair", #
"What Vusi's sister said",
###LEVEL 5###
"Unwise Judge",
]


#Creates FF profile
'''
fxProfile = webdriver.FirefoxProfile()

fxProfile.set_preference("browser.download.folderList",2)
fxProfile.set_preference("browser.download.manager.showWhenStarting",False)
fxProfile.set_preference("browser.helperApps.alwaysAsk.force", False);
fxProfile.set_preference("browser.download.dir","~/Downloads/ASb")
fxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv; application/pdf")
'''

#Opens FF to webpage using existing profile
profile = webdriver.FirefoxProfile('/home/jon-moreno/.mozilla/firefox/c7r83610.temp')
driver = webdriver.Firefox(profile)
driver.get("http://www.africanstorybook.org/")


#Performs initial search

try:
    elem = WebDriverWait(driver, 35).until(
        EC.visibility_of_element_located((By.ID, "mainSearchInput"))
    )
    #print("First Search Bar Visible")
except Exception as e:
    pass

elem = driver.find_element_by_id("mainSearchInput")
elem.send_keys(".")
elem.send_keys(Keys.ENTER)

#Waits for new search bar
try:
    elem = WebDriverWait(driver, 35).until(
        EC.visibility_of_element_located((By.ID, "storySearchId"))
    )
    #print("Second Search Bar Visible")
    elem.clear()
except Exception as e:
    pass

###Loop Here###
for book in books:
    elem = driver.find_element_by_id("storySearchId")
    elem.clear()
    elem.send_keys(book)
    elem.send_keys(Keys.ENTER)

    #Redoes Failed search
    try:
        elem = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "searchbar-not-found"))
        )
        print("Search Results Invisible ", book)
        elem = driver.find_element_by_id("storySearchId")
        elem.clear()
        elem.send_keys(book)
        elem.send_keys(Keys.ENTER)
    except:
        #print("Search Results Visible")
        
        #Gets ID from first result
        try:
            elem = elem.find_element_by_xpath('//*[@id="virtualBlock"]/ul/li/a')
            #print("Only one element")
            
            bookID = elem.get_attribute("onclick").lstrip('loadBook(').rstrip(");").split(",")
            #print(bookID)
            #bookID = bookID.lstrip('loadBook(').rstrip(");").split(",")
            bookID = int(bookID[0])
            
            '''
            url = "http://www.africanstorybook.org/read/downloadbook.php?id={}&d=0&a=1&layout=landscape".format(bookID)
            driver.get(url)
            driver.switch_to_alert().accept()
            '''

            #http://www.africanstorybook.org/read/downloadbook.php?id=19760&d=0&a=1&layout=landscape
            #file = urllib.URLopener()
            #file.retrieve("url", "/home/jon-moreno/Downloads/ASb")
            #file.retrieve(url, "/media/jon-moreno/Backup Data/Dropbox (Library for All)/ASb")

        except Exception as e:
            try:
                elem = elem.find_element_by_xpath('a//*[@id="virtualBlock"]/ul/li[1]/a')
                #print("There are multiple elements")
                
                bookID = elem.get_attribute("onclick")
                #print(bookID)
                bookID = bookID.lstrip('loadBook(').rstrip(");").split(",")
                bookID = int(bookID[0])
                
                #http://www.africanstorybook.org/read/downloadbook.php?id=19760&d=0&a=1&layout=landscape
                url = "http://www.africanstorybook.org/read/downloadbook.php?id={}&d=0&a=1&layout=landscape".format(bookID)
                file = urllib.URLopener()
                #file.retrieve("url", "/home/jon-moreno/Downloads/ASb")
                file.retrieve(url, "/media/jon-moreno/Backup Data/Dropbox (Library for All)/ASb")
            except Exception as e:
                print("Well, shoot.")
'''
    try:
        elem = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "virtualBlock"))
        )
        

    except Exception as e:
        #print("Search Results not Visible")
 '''   

##print(elem)
#elem = elem.find_element_by_class_name("item-link").get_attribute("onclick")

try:
    elem = elem.find_element_by_xpath('//*[@id="virtualBlock"]/ul/li/a')
    #print("Only one element")
    #print(elem.get_attribute("onclick"))
except Exception as e:
    try:
        elem = elem.find_element_by_xpath('a//*[@id="virtualBlock"]/ul/li[1]/a')
        #print("There are multiple elements")
        #print(elem.get_attribute("onclick"))
    except Exception as e:
        print("Well, shoot.")
        #raise e
        #driver.refresh()

driver.quit()

def download(elem):
    bookID = elem.get_attribute("onclick")
    #print(bookID)
    bookID = bookID.lstrip('loadBook(').rstrip(");").split(",")
    bookID = int(bookID[0])
    
    #http://www.africanstorybook.org/read/downloadbook.php?id=19760&d=0&a=1&layout=landscape
    url = "http://www.africanstorybook.org/read/downloadbook.php?id={}&d=0&a=1&layout=landscape".format(bookID)
    file = urllib.URLopener()
    #file.retrieve("url", "/home/jon-moreno/Downloads/ASb")
    file.retrieve(url, "/media/jon-moreno/Backup Data/Dropbox (Library for All)/ASb")

#//TODO Open FF profile that will put in correct folder
#//Loop for every book
#//Pray to RMS that it works

'''
css=tag#id[attribute='value']
css=tag.classname[attribute='value']
'''

