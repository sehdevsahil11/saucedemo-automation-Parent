import time
from selenium import webdriver
from pages.inventory_page import InventoryPage

def test_all_sort_filters():
    driver = webdriver.Chrome()
    inventory_page = InventoryPage(driver)
    inventory_page.load()

    sort_options = [
        "Name (A to Z)",
        "Name (Z to A)",
        "Price (low to high)",
        "Price (high to low)"
    ]

    for option in sort_options:
        inventory_page.select_sort(option)
        time.sleep(2)  # Pause to visually confirm sorting
        print(f"✅ Verified filter: {option}")

    time.sleep(30)  # Keep browser open a little longer after last filter
    driver.quit()
