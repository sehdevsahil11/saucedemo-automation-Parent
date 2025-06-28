from selenium.webdriver.common.by import By
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        # Assumes already on cart page
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(2)

    def finish_checkout(self):
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(5)
