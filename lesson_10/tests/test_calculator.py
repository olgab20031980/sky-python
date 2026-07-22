import sys
import os
import allure

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, current_dir)  # noqa: E402

from selenium import webdriver  # noqa: E402
from selenium.webdriver.chrome.options import Options  # noqa: E402
from pages.calculator_page import CalculatorPage  # noqa: E402


@allure.epic("UI Тестирование")
@allure.feature("Калькулятор")
@allure.story("Арифметические операции")
class TestCalculator:
    def setup_method(self):
        with allure.step("Инициализация браузера Chrome"):
            options = Options()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)

    def teardown_method(self):
        with allure.step("Закрыть браузер"):
            self.driver.quit()

    @allure.title("Тест медленного сложения 7 + 8 = 15")
    @allure.description(
        "Проверяет работу калькулятора с задержкой. "
        "Устанавливается задержка 45 секунд, вводятся числа 7 и 8, "
        "ожидается результат 15."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke", "calculator", "math")
    @allure.link(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html",
        name="Slow Calculator"
    )
    def test_slow_addition(self):
        with allure.step("Создать экземпляр страницы калькулятора"):
            calculator_page = CalculatorPage(self.driver)

        with allure.step("Открыть страницу калькулятора"):
            calculator_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Ввести выражение 7 + 8"):
            with allure.step("Нажать кнопку '7'"):
                calculator_page.click_button("7")
            with allure.step("Нажать кнопку '+'"):
                calculator_page.click_button("+")
            with allure.step("Нажать кнопку '8'"):
                calculator_page.click_button("8")

        with allure.step("Нажать кнопку '=' для получения результата"):
            calculator_page.click_button("=")

        with allure.step("Получить результат и проверить, что он равен 15"):
            result = calculator_page.get_result(expected_value=15, timeout=60)
            assert result == "15", f"Expected '15', got '{result}'"
