import time
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
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
# options.add_argument("--headless")
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
        name = itemContainer.find_element(By.CLASS_NAME, "title-hover").text
        newItem = Item(name, price, addToCart)
        items.append(newItem)

        print(newItem.name + " costing " + newItem.price)


def addToCart(items: list, driver: WebDriver):
    for item in items:
        print(str(items.index(item)) + " - " + item.name)
    idk = input("Enter the item number you want:")
    try:
        items[int(idk)].cartPointer.click()
        driver.find_element(By.ID, "item-detail-parent").find_element(By.CLASS_NAME, 'add-to-cart-button ').click()
    except Exception as e:
        print(e)
        print("Couldn't add " + str(items[idk].name) + " to cart")


def checkout(driver: WebDriver):
    time.sleep(0.5)
    cartButton = driver.find_element(By.CLASS_NAME, "cart-icon")
    cartButton.click()
    time.sleep(0.5)
    continueButton = driver.find_element(By.CLASS_NAME, "pay-cart-button")
    continueButton.click()
    time.sleep(0.5)
    loginButton = driver.find_element(By.CLASS_NAME, "login-btn-atrium")
    loginButton.click()


def fulfullment(firstName, lastInitial, phoneNumber, driver):
    firstName = "Bobby"
    lastInitial = "D"
    phoneNumber = "9144097471"
    cartButton = driver.find_element(By.CLASS_NAME, "cart-icon")
    cartButton.click()
    time.sleep(0.5)
    continueButton = driver.find_element(By.CLASS_NAME, "pay-cart-button")
    continueButton.click()
    time.sleep(0.5)

    fields = driver.find_elements(By.CSS_SELECTOR, "#parent > input")
    fields[0].send_keys(firstName)
    fields[1].send_keys(lastInitial)
    fields[2].send_keys(phoneNumber)

    driver.find_element(By.CLASS_NAME, "pay-button-site-has-signin").click()
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "pay-button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#parent > div.BottomContainer.sc-mWPeY.iESGGn.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.desktop-pay.sc-khfTgR.cOrHDO.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.pay-list-top-container.sc-koJQpy.hVbJaq.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div.pay-options-parent.sc-ckixc.ddwhEt.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div.click-cont.container.tile.atrium-3.sc-kQeHGI.lbGlam.sc-bwzfXH.cjHxAH.sc-bdVaJa.iHZvIS > div > div.detail-container-atrium.sc-fWMzbn.wlcrT.sc-bwzfXH.iaREIe.sc-bdVaJa.gRrvFh > div").click()


process(WebDriver, "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2195/5519", "7", items)

completed = False;
while not completed:
    addToCart(items,WebDriver)
    if (input("Are you done (Y or N): ") == "Y"):
        completed = True
checkout(WebDriver)
time.sleep(0.5)
signIn("Bkd7911",input("Type your RIT Password"),WebDriver)
input("Waiting for duo press any key when completed")
fulfullment("Bobby","D","9144097471", WebDriver)



