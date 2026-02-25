import os
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.api_login import get_auth_token
from pages.LoginPage import LoginPage


# -----------------------------
# CLI OPTION FOR AUTH TYPE
# -----------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--auth",
        action="store",
        default="api",
        help="Authentication method: api or ui"
    )


# -----------------------------
# BROWSER SETUP FIXTURE
# -----------------------------
@pytest.fixture(scope="function")
def setup(request):

    options = Options()

    # Headless by default (for CI)
    if os.getenv("HEADLESS", "true") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    request.cls.driver = driver
    yield
    driver.quit()


# -----------------------------
# PURE UI LOGIN FIXTURE
# -----------------------------
@pytest.fixture(scope="function")
def ui_login_user(setup, request):

    driver = request.cls.driver

    email = "gvd@test.com"
    password = "Gvd@1399"

    login = LoginPage(driver)
    login.load()
    login.enter_email(email)
    login.enter_password(password)
    login.click_login()

    yield


# -----------------------------
# PURE API LOGIN FIXTURE
# -----------------------------
@pytest.fixture(scope="function")
def api_login_user(setup, request):

    driver = request.cls.driver

    email = "gvd@test.com"
    password = "Gvd@1399"

    token = get_auth_token(email, password)

    driver.get("https://rahulshettyacademy.com/client")

    driver.execute_script(
        "window.localStorage.setItem('token', arguments[0]);",
        token
    )

    driver.refresh()

    yield


# -----------------------------
# DYNAMIC LOGIN FIXTURE
# -----------------------------
@pytest.fixture(scope="function")
def login_user(setup, request):

    auth_method = request.config.getoption("--auth")

    if auth_method == "api":
        request.getfixturevalue("api_login_user")

    elif auth_method == "ui":
        request.getfixturevalue("ui_login_user")

    else:
        raise ValueError("Invalid auth method. Use --auth=api or --auth=ui")

    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item.cls, "driver", None)
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Save screenshot locally (optional)
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )