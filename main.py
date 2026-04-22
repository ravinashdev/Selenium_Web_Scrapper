from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep, time


# Amazon
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.amazon.com/LIFXIZE-Helmet-Hanger-Rotation-Motorcycle/dp/B0B6P2GSWH/ref=sr_1_8?crid=3LOBS1DFQZTUF&dib=eyJ2IjoiMSJ9.ic0jB5fnVNQIQgUSOi-wFreGQ8S_uZgaftD11mRQ-RHwv-KqblV61sZkQ22Q1Nxo8MdE-LwzuQLN-GXJWkVS047aa67rZNHaV73-jPeCzXIJ_Y80fL2M0JFblR9YHJjyu5A_tsBipIdORbUvvnyaITe8imrWRTqtc6Xmtfi2Pq--ZcK7ivFTNJsWLNk5pb-IidzOl5-D-mJuxaUpDwn8QgjUtNTe_3AeOhPg4GJoNmk.c1cz9PAHbVLclnNBDF4tmqLnpsFx3LlfQNM6ecmom5A&dib_tag=se&keywords=indian%2Bmotorcycle&qid=1776832095&sprefix=Indian%2Bmoto%2Caps%2C350&sr=8-8&th=1")

amazon_dollar_price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
amazon_dollar_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
amazon_store_link = driver.find_element(By.XPATH, value="//*[@id='bylineInfo']").get_attribute("href")

print(amazon_dollar_price)
print(amazon_dollar_cents)
print(amazon_store_link)

input("Press Enter to close...")
driver.quit()

# Wikipedia
# Much cleaner than using Beautiful soup
user_input = input("What year brings you back? ").strip()
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# Have selenium hit the landing page then click on the appropriate link based on text
driver.get(f"https://en.wikipedia.org/wiki/Category:Lists_of_Billboard_Year-End_Hot_100_singles")
# Click on the link for the text with a given year
driver.find_element(By.LINK_TEXT, f"Billboard Year-End Hot 100 singles of {user_input}").click()
table = driver.find_element(By.CSS_SELECTOR, "table.wikitable")
top_100_rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
# print(top_100_rows)
top_100_list = []
for row in top_100_rows:
    # print(row)
    row_data = row.find_elements(By.TAG_NAME, "td")
    song = {
        "rank": row_data[0].text,
        "title": row_data[1].text,
        "artist": row_data[2].text,
    }
    top_100_list.append(song)
print(top_100_list)
input("Press Enter to close...")
driver.quit()

# Google Search
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(f"https://www.google.com")
google_search = driver.find_element(By.ID, "APjFqb")
google_search.send_keys("Buy a home in Pkuket Thailand Fazwaz")
sleep(10)
google_search.send_keys(Keys.RETURN)

input("Press Enter to close...")
driver.quit()


