from selenium import webdriver
from pages.logout_page import LogoutPage

def test_logout_process():
    driver = webdriver.Chrome()
    logout_page = LogoutPage(driver)

    logout_page.load()
    logout_page.go_to_product_details("Sauce Labs Backpack")
    logout_page.back_to_products()
    logout_page.open_menu()
    logout_page.logout()

    assert "saucedemo.com" in driver.current_url  # Basic check for logout success
    driver.quit()
