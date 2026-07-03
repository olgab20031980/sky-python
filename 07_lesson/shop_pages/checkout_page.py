from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")

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
