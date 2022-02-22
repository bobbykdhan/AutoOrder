import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def signIn(username, password, driver):
    time.sleep(0.5)
    cartButton = driver.find_element(By.CLASS_NAME, "cart-icon")
    cartButton.click()
    time.sleep(0.5)
    continueButton = driver.find_element(By.CLASS_NAME, "pay-cart-button")
    continueButton.click()
    time.sleep(1)
    loginButton = driver.find_element(By.CLASS_NAME, "login-btn-atrium")
    loginButton.click()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "_eventId_proceed").click()


