from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from shop_pages.login_page import LoginPage
from shop_pages.inventory_page import InventoryPage
from shop_pages.cart_page import CartPage
from shop_pages.checkout_page import CheckoutPage


class TestShop:

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_shop_checkout_total(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()

        cart_count = inventory_page.get_cart_count()
        assert cart_count == 3, f"Expected 3 items in cart, got {cart_count}"

        inventory_page.go_to_cart()

        cart_page = CartPage(self.driver)
        items_count = cart_page.get_cart_items_count()
        assert items_count == 3, f"Expected 3 items in cart, got {items_count}"

        cart_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_form("John", "Doe", "12345")

        total = checkout_page.get_total()

        expected_total = 58.29
        assert total == expected_total, (
            f"Expected total ${expected_total}, got ${total}"
        )

        print(f"Total: ${total}")
