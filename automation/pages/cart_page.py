from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

    def add_to_cart(self, item_name):
        button_id = f"add-to-cart-{item_name.lower().replace(' ', '-').replace('(', '').replace(')', '')}"
        self.driver.find_element(By.ID, button_id).click()
        time.sleep(1)

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3)

    def remove_from_cart(self, item_name):
        button_id = f"remove-{item_name.lower().replace(' ', '-').replace('(', '').replace(')', '')}"
        self.driver.find_element(By.ID, button_id).click()
        time.sleep(1)

    def is_item_in_cart(self, item_name):
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for item in cart_items:
            if item.text.strip().lower() == item_name.lower():
                return True
        return False

    def hold_browser(self, seconds=30):
        time.sleep(seconds)
