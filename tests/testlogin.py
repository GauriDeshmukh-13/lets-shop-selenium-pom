import pytest
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("setup")
class TestShop:

    def test_e2e_order(self):
        login = LoginPage(self.driver)
        login.load()
        login.enter_email("demo@gmail.com")
        login.enter_password("practiceautomation@123")
        login.click_login()

        url = self.driver.current_url
        assert 'dashboard' in url




