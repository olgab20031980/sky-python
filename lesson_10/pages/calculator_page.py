import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


@allure.epic("UI Тестирование")
@allure.feature("Калькулятор")
class CalculatorPage:

    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_DISPLAY = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.get(url)
        return self

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    @allure.step("Нажать кнопку '{value}'")
    def click_button(self, value):
        if value == "7":
            locator = self.BUTTON_7
        elif value == "8":
            locator = self.BUTTON_8
        elif value == "+":
            locator = self.BUTTON_PLUS
        elif value == "=":
            locator = self.BUTTON_EQUALS
        else:
            raise ValueError(f"Unknown button value: {value}")

        button = self.driver.find_element(*locator)
        button.click()
        return self

    @allure.step("Получить результат (ожидается: {expected_value})")
    def get_result(self, expected_value=None, timeout=60):
        result_element = self.driver.find_element(*self.RESULT_DISPLAY)

        if expected_value is not None:
            try:
                WebDriverWait(self.driver, timeout).until(
                    lambda driver: result_element.text == str(expected_value)
                )
            except TimeoutException:
                pass

        return result_element.text
