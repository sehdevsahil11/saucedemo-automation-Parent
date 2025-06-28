from selenium.webdriver.common.by import By
import time

class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def load_product(self, product_name):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        # Click on the product link by product name
        self.driver.find_element(By.LINK_TEXT, product_name).click()
        time.sleep(3)

    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text.strip()

    def get_product_description(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_desc").text.strip()

    def get_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_price").text.strip()

    def hold_browser(self, seconds=30):
        time.sleep(seconds)
