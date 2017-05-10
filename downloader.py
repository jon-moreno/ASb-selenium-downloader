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

#Opens FF to webpage
driver = webdriver.Firefox()
driver.get("http://www.africanstorybook.org/")

#Searches for book
elem = driver.find_element_by_id("mainSearchInput")
elem.send_keys(books[0])
elem.send_keys(Keys.RETURN)

#Waits until search results loaded
elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "storySearchId"))
    )

#Opens book searched for
elem = driver.find_element_by_id("storySearchId")
elem.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)

#Downloads book