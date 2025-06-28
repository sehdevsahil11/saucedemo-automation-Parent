from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.item_prices = (By.CLASS_NAME, "inventory_item_price")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def select_sort(self, visible_text):
        dropdown_element = self.driver.find_element(*self.sort_dropdown)
        select = Select(dropdown_element)
        select.select_by_visible_text(visible_text)
        time.sleep(2)  # just for demo/visual pause

    def sort_by_price_low_to_high(self):
        self.select_sort("Price (low to high)")

    def get_displayed_prices(self):
        price_elements = self.driver.find_elements(*self.item_prices)
        prices = [float(p.text.replace("$", "")) for p in price_elements]
        return prices
