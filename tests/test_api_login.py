import pytest

@pytest.mark.usefixtures("setup", "api_login_user")
class TestApiLogin:

    def test_dashboard_loaded(self):
        assert "dashboard" in self.driver.current_url