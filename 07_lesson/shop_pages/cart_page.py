from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def get_cart_item_names(self):
        items = self.driver.find_elements(*self.CART_ITEM_NAME)
        return [item.text for item in items]

    def click_checkout(self):
        checkout_button = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_button.click()
        return self
