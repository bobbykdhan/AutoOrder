from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Login import signIn

PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"


service = Service(PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://ondemand.rit.edu/menu/dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2162/5584/4")
input("waiting for site to load")

items = driver.find_elements(By.CLASS_NAME, "detail-container")
itemFeatures = []
for item in items:
    items.append(item.find_element(By.CLASS_NAME, "title-hover"))

# //div[@id='parent']/div/div/div[6]/div/div/a/div

for itemFeature in itemFeatures:
    print(itemFeature.text)

input("Done")