from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "/Users/bobby/Documents/Projects/AutoOrder/chromedriver"
service = Service(PATH)
options = webdriver.ChromeOptions()



def signIn(username, password):
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://mycourses.rit.edu/Shibboleth.sso/Login?entityID=https://shibboleth.main.ad.rit.edu/idp/shibboleth&target=https%3A%2F%2Fmycourses.rit.edu%2Fd2l%2FshibbolethSSO%2Flogin.d2l")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    print("Waiting for Duo...")




signIn()