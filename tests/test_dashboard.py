import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup","login_user")
class TestDashboard:

    def test_dashboard_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("dashboard"))
        assert "dashboard" in self.driver.current_url