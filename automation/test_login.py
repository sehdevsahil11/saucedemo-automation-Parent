from selenium import webdriver
import time

def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    time.sleep(30)  # wait 30 seconds so you can see the browser
    driver.quit()
