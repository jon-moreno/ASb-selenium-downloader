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

print(driver.find_element_by_class_name("searchbar"))
#print(driver.find_element_by_css_selector("form.searchbar.theme-background.searchbarHome.searchbar-active"))



#Performs initial search
try:
    elem = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.ID, "mainSearchInput"))
    )
    print("First Search Bar Located")
except Exception as e:
    pass

#elem = driver.find_element_by_id("mainSearchInput")
elem.send_keys(books[0])
elem.send_keys(Keys.ENTER)

#Waits for new search bar
try:
    elem = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.ID, "storySearchId"))
    )
    print("Second Search Bar Located")
except Exception as e:
    pass

#print(elem)

#Waits for search results
try:
    elem = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.CLASS_NAME, "item-link"))
    )
    print("Search Results Located")
except Exception as e:
    pass

#print(elem)
#elem = elem.find_element_by_class_name("item-link").get_attribute("onclick")

try:
    elem = elem.find_element_by_xpath('//*[@id="virtualBlock"]/ul/li/a')
    print("Only one element")
except Exception as e:
    try:
        elem = elem.find_element_by_xpath('a//*[@id="virtualBlock"]/ul/li[1]/a')
        print("There are multiple elements")
    except Exception as e:
        raise e


#css = "a.item-link.item-content.external.with-animation"
#elem = elem.find_element_by_css_selector(css)
#elem = elem.find_element_by_class_name("item-link.item-content.external.with-animation")
print(elem.get_attribute("onclick"))

#http://www.africanstorybook.org/read/downloadbook.php?id=19760&d=0&a=1&layout=landscape
#http://www.africanstorybook.org/read/downloadbook.php?id={ID}&d=0&a=1&layout=landscape

#//TODO Open FF profile that will put in correct folder
#//Loop for every book
#//Pray to RMS that it works

'''
css=tag#id[attribute=’value’]
css=tag.classname[attribute=’value’]
'''

