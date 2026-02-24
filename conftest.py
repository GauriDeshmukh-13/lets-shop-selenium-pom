import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from utils.data_reader import load_test_data

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.quit()

@pytest.fixture(scope="function")
def login_user(setup, request):
    driver = request.cls.driver

    login = LoginPage(driver)
    login.load()

    login_data = load_test_data("login_data.json")

    valid_user = next(
        data for data in login_data if data["expected_url"] is not None
    )

    login.enter_email(valid_user["email"])
    login.enter_password(valid_user["password"])
    login.click_login()

    yield