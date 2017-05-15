import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

books = [
"A very tall man",
"Colours of a rainbow",
"Frog and Snake",
"Friends (Zimbili Dlamini and Hlengiwe Zondi)",
"How tortoise got a crooked nose",
"Hyena, Hare and the basins",
"Lazy Anansi",
"Monkey and the drought",
"Palm tree (Simon Ipoo)",
"Porridge (Zimbili)",
"Which work is most important?",
"Chicken and Millipede",
"Africa Unity Race",
"Azizi the doll",
"Big blue bus",
"Curious Baby Elephant",
"Death visits Hupapa",
"Fire’s story",
"Goat, Dog and Cow",
"Hamisi’s lucky day",
"Jaaka the fisherman",
"My family and I",
"Ostrich and Lioness",
"Selemeng’s cats",
"The day the sun went away",
"Two little friends",
"Two thieves",
"Why Ajao was not buried",
"Wind (Ursula Nafula)",
"Adun the beautiful",
"Beloved daughter",
"Byantaka and the dead pot",
"Creature with two",
"Crushed louse",
"Fox and Rooster",
"Goat and Hyena’s knife",
"Holidays with grandmother",
"Hyena and Tortoise",
"Kalabushe the talkative",
"Maguru gives legs",
"Pontshibobo’s tree",
"The girl who got rich",
"Thunder and Lightning",
"Counting cabbages",
"Hare and Hyena",
"King Kayanja and his daughter",
"Magozwe",
"Share it fair",
"What Vusi’s sister said",
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

#Opens FF to webpage using profile
profile = webdriver.FirefoxProfile('/home/jon-moreno/.mozilla/firefox/c7r83610.temp')
driver = webdriver.Firefox(profile)
driver.get("http://www.africanstorybook.org/")

#Searches for book
elem = driver.find_element_by_id("mainSearchInput")
elem.send_keys(books[0])
elem.send_keys(Keys.ENTER)

#Waits until search results loaded
try:
    elem = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.ID, "storySearchId"))
    )
except Exception as e:
    pass


#Opens book searched for
elem = driver.find_element_by_id("storySearchId")
#elem.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
elem.send_keys(Keys.TAB*2, Keys.ENTER)


#Waits until book is loaded
elem = WebDriverWait(driver, 30).until(
        #EC.presence_of_element_located((By.CLASS_NAME, "menu-text"))
        EC.presence_of_element_located((By.ID, "headerBar"))
        #EC.presence_of_element_located((By.CLASS_NAME, "popup"))
        #EC.presence_of_element_located((By.CLASS_NAME, "imageBlock0"))

    )

'''
#Opens menu
elem = driver.find_element_by_class_name("menu-text")
elem.send_keys(Keys.TAB*2, Keys.ENTER)

#Waits until menu is loaded
elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "accordianRelatedStories"))
    )
elem = driver.find_element_by_id("accordianRelatedStories")

#Initiates Download
elem.send_keys(Keys.TAB*50, Keys.ENTER)
'''

'''So WTF are there 50 tabs? Because you have to tab through the non-visible <li>
in the menu. You can't click the download <li> directly, otherwise this would work:

elem = driver.find_element_by_xpath('//*[@id="bookPanel"]/li[6]')
elem.click()

This website makes me cry inside.'''

'''
#Goes back to search
elem = driver.find_element_by_id("storySearchId")
elem.clear()
elem.send_keys(books[1])
elem.send_keys(Keys.ENTER)
elem.send_keys(Keys.TAB*2, Keys.ENTER)'''


elem = driver.find_element_by_class_name("left")
elem.send_keys(Keys.ENTER)
'''
elem = driver.find_element_by_class_name("back")
elem.click()

elem = driver.find_element_by_class_name("back.link.icon-only")
elem.click()'''

#//TODO Open FF profile that will put in correct folder
#//Loop for every book
#//Pray to RMS that it works