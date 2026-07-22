import sys
import os

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, current_dir)  # noqa: E402

from selenium import webdriver  # noqa: E402
from selenium.webdriver.chrome.options import Options  # noqa: E402
from pages.calculator_page import CalculatorPage  # noqa: E402


class TestCalculator:

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_slow_addition(self):
        calculator_page = CalculatorPage(self.driver)
        calculator_page.open()
        calculator_page.set_delay(45)
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
        result = calculator_page.get_result(expected_value=15, timeout=60)
        assert result == "15", f"Expected '15', got '{result}'"
