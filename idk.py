""" 
file: .py
description:
language: python3
author: Bobby Dhanoolal @ RIT.EDU
"""


ritz = "https://ondemand.rit.edu/menu/dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2169/4101"
cad = "https://ondemand.rit.edu/menu/dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2166/3402"
commons = "https://ondemand.rit.edu/menu/dc9df36d-8a64-42cf-b7c1-fa041f5f3cfd/2159/3308"



checkout = "https://ondemand.rit.edu/fulfillment"
summary = "https://ondemand.rit.edu/summary"
payment  = "https://ondemand.rit.edu/payment"

from selenium import webdriver

PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"
driver = webdriver.Chrome(PATH)


driver.get(ritz)