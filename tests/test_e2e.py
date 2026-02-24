import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Product_Page import ProductPage
from pages.Cart_Page import CartPage

@pytest.mark.usefixtures("setup", "login_user")
class TestCartFlow:

    def add_products_to_cart(self):
        add_products = ProductPage(self.driver)
        add_products.add_product_to_cart("IPHONE 13 PRO")
        add_products.go_to_cart()

        cart = CartPage(self.driver)
        product_names = cart.get_cart_product_names()
        assert "IPHONE 13 PRO" in product_names
