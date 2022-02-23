import time
from dataclasses import dataclass

from selenium.webdriver.chrome.webdriver import WebDriver
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


# Initialize the Selenium WebDriver and the Wait object.
PATH = "/Users/bobby/Library/Mobile Documents/com~apple~CloudDocs/Documents/Projects/AutoOrder/chromedriver"
service = Service(PATH)
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 150, poll_frequency=1)

# Initialize the store inventory
global items
items = []


def searchForItems():
    """Searches for items in the store. Creates an updated a list of items."""

    # Waits for the store to load
    print("Searching for items")
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "detail-container")))

    # Gets the list of all elements with a class name of "detail-container"
    itemContainers = driver.find_elements(By.CLASS_NAME, "detail-container")

    # Iterates through each element and creates an Item object for each item
    for itemContainer in itemContainers:
        # Gets the bottom container of the detail
        bottomContainer = itemContainer.find_element(By.CLASS_NAME, "bottom-container")

        # Finds the name, price and cart element of the item and creates an Item object
        price = bottomContainer.text.split("\n")[0]
        cartPointer = bottomContainer.find_element(By.CLASS_NAME, "add-to-cart-text")
        name = itemContainer.find_element(By.CLASS_NAME, "title-hover").text
        newItem = Item(name, price, cartPointer)

        # adds all items to the list of items
        items.append(newItem)


def addToCart(itemIndex: int = None):
    """Adds an item to the cart."""
    # If no item index is given, ask the user for one. Otherwise, use the given index.
    # TODO: add the ability to add items without waiting for user input

    if itemIndex is None:
        # Iterates through each item in the list of items and prints the name and index

        for item in items:
            print(str(items.index(item)) + " - " + item.name)
        print("999 - To not add an item")
        # Asks the user for the index of the item they want to add

        itemIndex = int(input("Enter the index of the item you want to add to cart: \n"))

    # TODO: Add functionality to add items with modifiers
    # Checks if the user doesn't want to add an item
    if itemIndex != 999:
        try:
            # Adds the item to the cart
            items[itemIndex].cartPointer.click()
            wait.until(ec.visibility_of_element_located((By.ID, "item-detail-parent")))
            idk = driver.find_element(By.ID, "item-detail-parent")
            idk.find_element(By.CLASS_NAME, 'add-to-cart-button').click()
            print("Added " + items[itemIndex].name + " to cart")

        except Exception as e:
            # Catches any errors and prints the error
            print(e)
            print("Couldn't add " + str(items[itemIndex].name) + " to cart")


def selectCategory():
    """Allows the user to change the category."""
    # Clears the list of items
    items.clear()

    # Iterates through each category and prints the name and index
    driver.find_element(By.CSS_SELECTOR,
                        "#parent > div.TopContainer.sc-bRbqnn.eWYGcP.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.context-bar.sc-fFTYTi.gkytGs.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.back-link-container.sc-MYvYT.dBNCYJ.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > a > div.sc-bIKvTM.ikcqfa.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS").click()
    subMenus = driver.find_elements(By.CLASS_NAME, "detail-container")
    index = 0
    for menu in subMenus:
        print(str(index) + " - " + menu.text)
        index += 1
    # Asks the user for the index of the category they want to select and then clicks it
    choice = input("Choose the menu you want to shop from: \n")
    subMenus[int(choice)].click()
    print("Reindexing items\n")
    # Waits for the store to load and searches the site for the items
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "detail-container")))
    searchForItems(driver)


def signIn(username, password, driver):
    """Signs in to Shibboleth using the given username and password."""

    # Waits until the cart icon is visible and clicks it
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "cart-icon")))
    driver.find_element(By.CLASS_NAME, "cart-icon").click()

    # Waits until the checkout icon is visible and clicks it
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "pay-cart-button")))
    driver.find_element(By.CLASS_NAME, "pay-cart-button").click()

    # Waits until the login icon is visible and clicks it
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "login-btn-atrium")))
    driver.find_element(By.CLASS_NAME, "login-btn-atrium").click()

    # Waits until the username input is visible, enters the username, password and clicks the login button
    wait.until(ec.visibility_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "_eventId_proceed").click()



def fulfillment(firstName, lastInitial, phoneNumber):
    """Fulfills the order."""

    # Clicks the cart button, waits for the checkout button to appear and clicks it
    driver.find_element(By.CLASS_NAME, "cart-icon").click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "pay-cart-button")))
    driver.find_element(By.CLASS_NAME, "pay-cart-button").click()

    # Waits for the fulfillment page to load and then fills out the form
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#parent > input")))
    fields = driver.find_elements(By.CSS_SELECTOR, "#parent > input")

    # Fills out the fields
    fields[0].send_keys(firstName)
    fields[1].send_keys(lastInitial)
    fields[2].send_keys(phoneNumber)

    # Clicks the submit button at the end of the fulfillment form
    driver.find_element(By.CLASS_NAME, "pay-button-site-has-signin").click()

    # Clicks the finalize button, waits for the payment buttons to load, and selects the RIT Dining Dollars method
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "pay-button")))
    driver.find_element(By.CLASS_NAME, "pay-button").click()
    finalCheckoutSelector = "#parent > div.BottomContainer.sc-mWPeY.iESGGn.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.desktop-pay.sc-khfTgR.cOrHDO.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.pay-list-top-container.sc-koJQpy.hVbJaq.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div.pay-options-parent.sc-ckixc.ddwhEt.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div.click-cont.container.tile.atrium-3.sc-kQeHGI.lbGlam.sc-bwzfXH.cjHxAH.sc-bdVaJa.iHZvIS > div > div.detail-container-atrium.sc-fWMzbn.wlcrT.sc-bwzfXH.iaREIe.sc-bdVaJa.gRrvFh > div"
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, finalCheckoutSelector)))
    driver.find_element(By.CSS_SELECTOR, finalCheckoutSelector).click()

    # Waits for the text receipt button to load and clicks it
    textReceiptSelector = "#parent > div.BottomContainer.sc-mWPeY.iESGGn.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div.additional-options-container.sc-ePZHVD.fphWHk.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div > div:nth-child(3) > button"
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, textReceiptSelector)))
    driver.find_element(By.CSS_SELECTOR, textReceiptSelector).click()

    # Waits for the send button to load and clicks it
    sendSelector = "#receipt-modal > div.receipt-modal-parent.sc-bmyXtO.lkstDj.sc-frDJqD.bDtUxi.sc-ksYbfQ.kYqsUP.sc-TOsTZ.cESxnL > div.sc-kaNhvL.fPGvtj.sc-bdVaJa.gRrvFh > button"
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, sendSelector)))
    driver.find_element(By.CSS_SELECTOR, sendSelector).click()


def main():
    """ Main function that runs the program."""

    # Asks the user for their first name, last initial, phone number, username, and password
    username, password = input("Enter your RIT username: \n"), input("Enter your RIT password: \n")
    firstName = input("Enter your first name: \n")
    lastInitial = input("Enter your last initial: \n")
    phoneNumber = input("Enter your phone number: \n")

    # TODO: Add a menu for the user to select from the open stores
    # Asks the user for the site they want to shop from
    print("Example: http://ondemand.rit.edu/menu/dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2166/3402")
    print("This is the part you are entering: 'dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2166/3402'")
    store = input("Enter the URL of the store you want to shop from (After the 'menu/' part): \n")

    # Opens the browser to the store the user wants to shop from
    driver.get("https://ondemand.rit.edu/menu/" + store + "/" + "0")

    # Waits for the site to load and calls the selectCategory function
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "detail-container")))
    selectCategory()

    # Calls the addToCart function and asks the user if they wish to continue shopping, change the category, or checkout
    while True:
        addToCart()
        choice = input(
            "Press Y if you are done adding to cart, Press C if you wish to choose another category, Press any key to keep selecting")
        if (choice == "Y"):
            break
        elif choice == "C":
            # Calls the selectCategory function for the user to change their category
            selectCategory(driver)

    print("Logging in\n")

    # Calls the signIn function to log the user in
    signIn(username, password)
    input("Waiting for duo press any key when complete")

    # Calls the fulfillment function to complete the purchase after the cart container is loaded
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, "cart-link-container")))
    print("Fulfilling order\n")
    fulfillment(firstName, lastInitial, phoneNumber)
    print("Done placing order\n")


if __name__ == "__main__":
    main()
