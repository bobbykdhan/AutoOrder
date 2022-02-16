

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import Login

PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"


service = Service(PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

Login.signIn()

input("prompt")
ondemand = "https://ondemand.rit.edu"

ritz = "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2169/4101"
cad = "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2166/3402"
commons = "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2159/3308"
inn = "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2682/5465"
mid = "dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2164/3400"


checkout = "https://ondemand.rit.edu/fulfillment"
summary = "https://ondemand.rit.edu/summary"
payment = "https://ondemand.rit.edu/payment"




driver.get(ondemand)


test = driver.find_elements(By.ID, "pickup-0")

prompt = input("press enter")
print(test)
from selenium.webdriver import ActionChains

#
#
# driver.get(ondemand + "/menu/" + commons + "/4")
# prompt = input("press enter")


#element = driver.find_element(By.CSS_SELECTOR, "#detail-containertile\ item_5f2d5994a3bbc4000d2fae1e > div.bottom-container.sc-bnOsYM.livFwd.sc-bwzfXH.hKiLMS.sc-bdVaJa.iHZvIS > div.add-to-cart-text.sc-AhSAr.czaKAt.sc-gqjmRU.kKsieB")

# element = driver.find_element(By.CLASS_NAME,"add-to-cart-text sc-ioBwqd cumCEK sc-gqjmRU kKsieB")
#
# element.click()
# prompt = input("press enter")
# element = driver.find_element(By.CSS_SELECTOR, "#item-details-button-container > button")
# element.click()

# ActionChains(driver).click(element).perform()