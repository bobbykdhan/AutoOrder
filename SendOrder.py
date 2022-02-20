import time
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
options.add_argument("--headless")
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


def addToCart(items: list, driver: WebDriver):

    for item in items:
        print(str(items.index(item)) + " - " + item.name)
    idk = input("What do you want")
    try:
        items[int(idk)].cartPointer.click()
        driver.find_element(By.ID, "item-detail-parent").find_element(By.CLASS_NAME, 'add-to-cart-button ').click()
    except Exception as e:
        print(e)
        print("Couldn't add " + str(items[idk].name) + " to cart")


process(WebDriver, "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2195/5519", "7", items)


def checkout(driver: WebDriver):
    cartButton = driver.find_element(By.CLASS_NAME, "cart-icon")
    cartButton.click()
    time.sleep(0.5)
    continueButton = driver.find_element(By.CLASS_NAME, "pay-cart-button")
    continueButton.click()
    time.sleep(0.5)
    loginButton = driver.find_element(By.CLASS_NAME, "login-btn-atrium")
    loginButton.click()

def fulfullment(driver):


    firstName = "Bobby"
    lastInitial = "D"
    phoneNumber = "9144097471"
    driver.get("https://ondemand.rit.edu/fulfillment")
    wait = WebDriverWait(driver, 150, poll_frequency=1)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "topContainer")))
    driver.find_element(By.CLASS_NAME, "input-text firstName").send_keys(firstName)
    driver.find_element(By.CLASS_NAME, "input-text lastInitial").send_keys(lastInitial)
    driver.find_element(By.CLASS_NAME, "input-text phone-number").send_keys(phoneNumber)
    driver.find_element(By.CLASS_NAME, "pay-button-site-has-signin").click()
    input("Look")
    driver.get("https://ondemand.rit.edu/payment")









addToCart(items,WebDriver)
input("Hi again")
checkout(WebDriver)
input("waiting for rit login")
signIn("bkd7911", input("Password"), WebDriver)
input("waiting for duo still press any key")
# fulfullment(WebDriver)


#
# cartButton = WebDriver.find_element(By.CLASS_NAME, "cart-icon")
# cartButton.click()
#
# time.sleep(1)
# continueButton = WebDriver.find_element(By.CLASS_NAME, "pay-cart-button")
# continueButton.click()
#
