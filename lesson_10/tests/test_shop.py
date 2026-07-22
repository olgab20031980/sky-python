import sys
import os
import allure

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, current_dir)  # noqa: E402

from selenium import webdriver  # noqa: E402
from selenium.webdriver.firefox.options import Options  # noqa: E402
from selenium.webdriver.firefox.service import Service  # noqa: E402
from webdriver_manager.firefox import GeckoDriverManager  # noqa: E402
from pages.shop_page import (  # noqa: E402
    LoginPage,
    InventoryPage,
    CartPage,
    CheckoutPage
)


@allure.epic("UI Тестирование")
@allure.feature("Интернет-магазин")
@allure.story("Оформление заказа")
class TestShop:
    def setup_method(self):
        with allure.step("Инициализация браузера Firefox"):
            options = Options()
            options.add_argument("--start-maximized")
            service = Service(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service, options=options)
            self.driver.implicitly_wait(5)

    def teardown_method(self):
        with allure.step("Закрыть браузер"):
            self.driver.quit()

    @allure.title("Тест оформления заказа с проверкой итоговой суммы")
    @allure.description(
        "Проверяет полный сценарий оформления заказа в интернет-магазине: "
        "1. Авторизация под пользователем standard_user "
        "2. Добавление 3 товаров в корзину (рюкзак, футболка, комбинезон) "
        "3. Проверка количества товаров в корзине "
        "4. Переход в корзину и проверка количества "
        "5. Заполнение формы доставки "
        "6. Проверка итоговой суммы (должна быть 58.29)"
    )
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke", "e-commerce", "checkout", "critical")
    @allure.link("https://www.saucedemo.com/", name="Sauce Demo")
    @allure.issue("https://github.com/your-repo/issues/1", name="Issue #1")
    @allure.testcase(
        "https://github.com/your-repo/testcases/TC-001",
        name="Test Case TC-001"
    )
    def test_shop_checkout_total(self):
        with allure.step("Шаг 1: Авторизация в магазине"):
            with allure.step("Открыть страницу входа"):
                login_page = LoginPage(self.driver)
                login_page.open()

            with allure.step(
                "Ввести логин 'standard_user' и пароль 'secret_sauce'"
            ):
                login_page.login("standard_user", "secret_sauce")

        with allure.step("Шаг 2: Добавление товаров в корзину"):
            inventory_page = InventoryPage(self.driver)

            with allure.step("Добавить рюкзак"):
                inventory_page.add_backpack_to_cart()

            with allure.step("Добавить футболку"):
                inventory_page.add_bolt_tshirt_to_cart()

            with allure.step("Добавить комбинезон"):
                inventory_page.add_onesie_to_cart()

        with allure.step("Шаг 3: Проверка количества товаров в корзине"):
            cart_count = inventory_page.get_cart_count()
            with allure.step(
                f"Проверить, что в корзине 3 товара "
                f"(фактически: {cart_count})"
            ):
                assert cart_count == 3, f"Expected 3 items, got {cart_count}"

        with allure.step("Шаг 4: Переход в корзину и проверка"):
            with allure.step("Перейти в корзину"):
                inventory_page.go_to_cart()

            cart_page = CartPage(self.driver)
            items_count = cart_page.get_cart_items_count()
            # Строка 91 - исправлена (разбита на 2 строки)
            with allure.step(
                f"Проверить, что в корзине 3 товара "
                f"(фактически: {items_count})"
            ):
                assert items_count == 3, f"Expected 3 items, got {items_count}"

        with allure.step("Шаг 5: Оформление заказа"):
            with allure.step("Нажать кнопку 'Checkout'"):
                cart_page.click_checkout()

            checkout_page = CheckoutPage(self.driver)

            with allure.step("Заполнить форму доставки (John, Doe, 12345)"):
                checkout_page.fill_checkout_form("John", "Doe", "12345")

        with allure.step("Шаг 6: Проверка итоговой суммы"):
            total = checkout_page.get_total()
            expected_total = 58.29

            with allure.step(
                f"Сумма: ${expected_total} "
                f"(факт: ${total})"
            ):
                assert total == expected_total, (
                    f"Expected total ${expected_total}, got ${total}"
                )
