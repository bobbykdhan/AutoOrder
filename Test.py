import time


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"


service = Service(PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)



driver.get("https://www.reddit.com/")

htmltext = driver.page_source



# Scroll page to load whole content
# last_height = driver.execute_script("return document.body.scrollHeight")
# for i in range(0,1):
#     # Scroll down to the bottom.
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # Wait to load the page
#     time.sleep(2)
#     # Calculate new scroll height and compare with last height.
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height



soup = BeautifulSoup(htmltext, "html.parser")

imgList = []

try:
    for img in soup.find_all('img', alt=True):
        print(img['src'])
        imgList.append(img['src'])
        driver.get(img['src'])
        time.sleep(1)
except:
    print("Out of images")




