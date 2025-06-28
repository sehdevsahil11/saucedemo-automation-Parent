from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout_process():
    driver = webdriver.Chrome()

    # Load inventory page and login
    inventory_page = InventoryPage(driver)
    inventory_page.load()

    # Add item to cart and go to cart
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    # Proceed with checkout steps
    checkout_page = CheckoutPage(driver)
    checkout_page.start_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    driver.quit()
