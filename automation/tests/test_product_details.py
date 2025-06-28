from selenium import webdriver
from pages.product_details_page import ProductDetailsPage

def test_product_details_page():
    driver = webdriver.Chrome()
    product_page = ProductDetailsPage(driver)

    product_name = "Sauce Labs Backpack"
    product_page.load_product(product_name)

    assert product_page.get_product_name() == product_name, "Product name does not match"
    assert len(product_page.get_product_description()) > 0, "Product description is empty"
    assert product_page.get_product_price().startswith("$"), "Product price is not shown correctly"

    product_page.hold_browser(30)  # Hold browser open for 30 seconds
    driver.quit()
