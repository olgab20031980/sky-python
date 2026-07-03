from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:

    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        button = self.driver.find_element(*self.ADD_TO_CART_BACKPACK)
        button.click()
        return self

    def add_bolt_tshirt_to_cart(self):
        button = self.driver.find_element(*self.ADD_TO_CART_BOLT_TSHIRT)
        button.click()
        return self

    def add_onesie_to_cart(self):
        button = self.driver.find_element(*self.ADD_TO_CART_ONESIE)
        button.click()
        return self

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def go_to_cart(self):
        cart_link = self.driver.find_element(*self.SHOPPING_CART_LINK)
        cart_link.click()
        return self
