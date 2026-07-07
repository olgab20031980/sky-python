from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        return self


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


class CartPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def click_checkout(self):
        checkout_button = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_button.click()
        return self


class CheckoutPage:

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_input = self.driver.find_element(*self.FIRST_NAME_INPUT)
        first_name_input.send_keys(first_name)
        last_name_input = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)
        postal_code_input = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_input.send_keys(postal_code)
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()
        return self

    def get_total(self):
        total_element = self.driver.find_element(*self.TOTAL_LABEL)
        total_text = total_element.text
        total_value = total_text.replace("Total: $", "").strip()
        return float(total_value)
