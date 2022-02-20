from dataclasses import dataclass

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Login import signIn
from selenium.webdriver.support import expected_conditions as ec


@dataclass
class Item:
    """Class for keeping track of an item in store inventory."""
    name: str
    price: float
    cartPointer: WebElement


PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"

service = Service(PATH)
options = webdriver.ChromeOptions()
WebDriver = webdriver.Chrome(service=service, options=options)

items = []


def process(driver: WebDriver, store: str, subMenu: str, items: list):
    wait = WebDriverWait(driver, 150, poll_frequency=1)

    driver.get("https://ondemand.rit.edu/menu/" + store + '/' + subMenu)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "top-container")))

    itemContainers = driver.find_elements(By.CLASS_NAME, "top-container")

    for itemContainer in itemContainers:
        bottomContainer = itemContainer.find_element(By.CLASS_NAME, "bottom-container")

        price = bottomContainer.text.split("\n")[0]
        addToCart = bottomContainer.find_element(By.CLASS_NAME, "add-to-cart-text")
        # addToCart.click()

        name = itemContainer.find_element(By.CLASS_NAME, "title-hover").text

        newItem = Item(name, price, addToCart)
        items.append(newItem)

        print(newItem.name + " costing " + newItem.price)


process(WebDriver, "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2195/5519", "7", items)

idk = ""
while (idk != "q"):
    for item in items:
        print(str(items.index(item)) + " - " + item.name)
    idk = input("What do you want / press q to end")
    try:
        items[int(idk)].cartPointer.click()
        WebDriver.find_element(By.ID, "item-detail-parent").find_element(By.CLASS_NAME, 'add-to-cart-button ').click()


    except Exception as e:
        print(e)
        print("couldnt find the cart button 0")
