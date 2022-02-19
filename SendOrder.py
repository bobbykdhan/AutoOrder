from dataclasses import dataclass

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Login import signIn


@dataclass
class Item:
    """Class for keeping track of an item in store inventory."""
    name: str
    price: float
    cartPointer: WebElement


PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"

service = Service(PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://ondemand.rit.edu/menu/dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2163/5621/5")
input("waiting for site to load")

itemElements = driver.find_elements(By.CLASS_NAME, "top-container")
items = []
count = 0
for item in itemElements:

    bottomContainer = item.find_element(By.CLASS_NAME, "bottom-container")
    name = item.find_element(By.CLASS_NAME, "title-hover").text
    print("added: " + name)

    items.append(Item(name, bottomContainer.find_element(By.CLASS_NAME, "amount").text,
                      bottomContainer.find_element(By.CLASS_NAME, "add-to-cart-text")))

    try:
        items[count].cartPointer.click()
        driver.find_element(By.CLASS_NAME, "BottomContainer").find_element(By.CLASS_NAME, 'add-to-cart-button ').click()

    except:
        print("\tcouldnt find the second one")

    print(items[count].name + " costing " + items[count].price)
    count += 1
