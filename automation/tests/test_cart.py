from selenium import webdriver
from pages.cart_page import CartPage
import time

def test_add_and_remove_single_item():
    driver = webdriver.Chrome()
    cart_page = CartPage(driver)

    cart_page.load()
    cart_page.add_to_cart("Sauce Labs Backpack")
    cart_page.go_to_cart()

    assert cart_page.is_item_in_cart("Sauce Labs Backpack"), "Item was not found in the cart"

    cart_page.remove_from_cart("Sauce Labs Backpack")
    assert not cart_page.is_item_in_cart("Sauce Labs Backpack"), "Item was not removed from the cart"

    cart_page.hold_browser(30)  # Hold browser open for 30 seconds
    driver.quit()
