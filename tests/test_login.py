import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.data_reader import load_test_data
from pages.LoginPage import LoginPage


test_data = load_test_data("login_data.json")


@pytest.mark.usefixtures("setup")
class TestShop:

    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):

        login = LoginPage(self.driver)
        login.load()
        login.enter_email(data["email"])
        login.enter_password(data["password"])
        login.click_login()

        wait = WebDriverWait(self.driver, 10)

        if data["expected_url"]:
            wait.until(EC.url_contains(data["expected_url"]))
            assert data["expected_url"] in self.driver.current_url
        else:
            error_message = login.get_error_message()
            assert data["expected_error"] in error_message
