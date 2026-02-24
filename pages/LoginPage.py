from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    #-----LOCATORS-------
    email = (By.CSS_SELECTOR, "#userEmail")
    password = (By.CSS_SELECTOR, "#userPassword")
    login_button = (By.CSS_SELECTOR, "#login")
    login_error = (By.CSS_SELECTOR, ".toast-message")

    #-----ACTIONS-----
    def load(self):
        self.driver.get("https://rahulshettyacademy.com/client/#/auth/login")

    def enter_email(self,email_id):
        email = self.wait.until(EC.visibility_of_element_located(self.email))
        email.send_keys(email_id)

    def enter_password(self,pwd):
        password = self.wait.until(EC.visibility_of_element_located(self.password))
        password.send_keys(pwd)

    def click_login(self):
        click = self.wait.until(EC.element_to_be_clickable(self.login_button))
        self.driver.execute_script("arguments[0].click();", click)

    def get_error_message(self):
        login_error = self.wait.until(EC.presence_of_element_located(self.login_error))
        return login_error.text