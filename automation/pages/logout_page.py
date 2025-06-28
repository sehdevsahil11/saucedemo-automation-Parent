from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def go_to_product_details(self, product_name):
        # Find all product titles and click the matching one
        product_titles = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for title in product_titles:
            if title.text.strip() == product_name:
                title.click()
                time.sleep(2)
                return
        raise Exception(f"Product '{product_name}' not found on inventory page.")

    def back_to_products(self):
        self.driver.find_element(By.ID, "back-to-products").click()
        time.sleep(1)

    def open_menu(self):
        menu_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_btn.click()
        time.sleep(1)

    def logout(self):
        logout_link = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
        time.sleep(2)
