from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    driver.quit()
