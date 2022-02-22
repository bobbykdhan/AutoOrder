import time
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Login import signIn
from selenium.webdriver.support import expected_conditions as ec
from secrets import *


@dataclass
class Item:
    """Class for keeping track of an item in store inventory."""
    name: str
    price: float
    cartPointer: WebElement


PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"
service = Service(PATH)
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--headless")
WebDriver = webdriver.Chrome(service=service, options=options)
global items
items = []


def searchForItems(driver: WebDriver):
    wait = WebDriverWait(driver, 50, poll_frequency=1)
    print("Searching for items")
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "detail-container")))

    itemContainers = driver.find_elements(By.CLASS_NAME, "detail-container")

    for itemContainer in itemContainers:
        bottomContainer = itemContainer.find_element(By.CLASS_NAME, "bottom-container")
        price = bottomContainer.text.split("\n")[0]
        addToCart = bottomContainer.find_element(By.CLASS_NAME, "add-to-cart-text")
        name = itemContainer.find_element(By.CLASS_NAME, "title-hover").text
        newItem = Item(name, price, addToCart)
        items.append(newItem)



def addToCart(items: list, driver: WebDriver, itemIndex: int = None):
    """Adds an item to the cart."""
    if itemIndex is None:
        for item in items:
            print(str(items.index(item)) + " - " + item.name)
        print("999 - To not add an item")
        itemIndex = int(input("Enter the index of the item you want to add to cart: \n"))
    if itemIndex != 999:
        try:
            items[itemIndex].cartPointer.click()

            wait.until(ec.visibility_of_element_located((By.ID, "item-detail-parent")))
            idk = driver.find_element(By.ID, "item-detail-parent")
            idk.find_element(By.CLASS_NAME, 'add-to-cart-button').click()
            print("Added " + items[itemIndex].name + " to cart")


            selector = "modifiers"
        except Exception as e:
            print(e)
            print("Couldn't add " + str(items[itemIndex].name) + " to cart")



def fulfillment(firstName, lastInitial, phoneNumber, driver):
   
    cartButton = driver.find_element(By.CLASS_NAME, "cart-icon")
    cartButton.click()
    time.sleep(0.5)
    continueButton = driver.find_element(By.CLASS_NAME, "pay-cart-button")
    continueButton.click()
    wait = WebDriverWait(driver, 150, poll_frequency=1)

    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#parent > input")))
    fields = driver.find_elements(By.CSS_SELECTOR, "#parent > input")

    fields[0].send_keys(firstName)
    fields[1].send_keys(lastInitial)
    fields[2].send_keys(phoneNumber)

    finalCheckoutSelector = "#parent > div.BottomContainer.sc-mWPeY.iESGGn.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.desktop-pay.sc-khfTgR.cOrHDO.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.pay-list-top-container.sc-koJQpy.hVbJaq.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div.pay-options-parent.sc-ckixc.ddwhEt.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div.click-cont.container.tile.atrium-3.sc-kQeHGI.lbGlam.sc-bwzfXH.cjHxAH.sc-bdVaJa.iHZvIS > div > div.detail-container-atrium.sc-fWMzbn.wlcrT.sc-bwzfXH.iaREIe.sc-bdVaJa.gRrvFh > div"

    driver.find_element(By.CLASS_NAME, "pay-button-site-has-signin").click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "pay-button")))
    driver.find_element(By.CLASS_NAME, "pay-button").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, finalCheckoutSelector)))

    driver.find_element(By.CSS_SELECTOR, finalCheckoutSelector).click()

    textReceiptSelector = "#parent > div.BottomContainer.sc-mWPeY.iESGGn.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.additional-options-container.sc-ePZHVD.fphWHk.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div:nth-child(3) > button"
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, textReceiptSelector)))

    driver.find_element(By.CSS_SELECTOR, textReceiptSelector).click()

    sendSelector = "#receipt-modal > div.receipt-modal-parent.sc-bmyXtO.lkstDj.sc-frDJqD.bDtUxi.sc-ksYbfQ.kYqsUP.sc-TOsTZ.cESxnL > div.sc-kaNhvL.fPGvtj.sc-bdVaJa.gRrvFh > button"
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sendSelector)))

    driver.find_element(By.CSS_SELECTOR, sendSelector).click()


def selectMenu(driver: WebDriver):
    items.clear()
    driver.find_element(By.CSS_SELECTOR,
                        "#parent > div.TopContainer.sc-bRbqnn.eWYGcP.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.context-bar.sc-fFTYTi.gkytGs.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.back-link-container.sc-MYvYT.dBNCYJ.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > a > div.sc-bIKvTM.ikcqfa.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS").click()
    subMenus = driver.find_elements(By.CLASS_NAME, "detail-container")
    index = 0
    for menu in subMenus:
        print(str(index) + " - " + menu.text)
        index += 1
    choice = input("Choose the menu you want to shop from: \n")
    subMenus[int(choice)].click()
    print("Reindexing items")


    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "detail-container")))

    searchForItems(driver)


def main(driver: WebDriver, items: list, username: str, password: str, firstName: str, lastInitial: str,
         phoneNumber: str, menu: str, subMenu: str):
    done = False
    while not done:
        addToCart(items, WebDriver)
        choice = input(
            "Press Y if you are done adding to cart, Press C if you wish to choose another category, Press any key to keep selecting")
        if (choice == "Y"):
            done = True
        elif choice == "C":
            selectMenu(driver)

    time.sleep(0.5)
    signIn(username, password, WebDriver)
    input("Waiting for duo press any key when complete")


    wait.until(ec.presence_of_element_located((By.CLASS_NAME, "cart-link-container")))
    print("Fulfilling order")
    fulfillment(firstName, lastInitial, phoneNumber, WebDriver)
    print("Done")




WebDriver.get("https://ondemand.rit.edu/menu/dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2195/5519/0")
wait = WebDriverWait(WebDriver, 150, poll_frequency=1)

wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "detail-container")))

selectMenu(WebDriver)

main(WebDriver, items, USERNAME, PASSWORD, "Bobby", "D", PHONE, "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2195/5519", "7")
