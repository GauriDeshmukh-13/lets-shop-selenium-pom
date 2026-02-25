import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #----LOCATORS-----
    Product_Cards = (By.CSS_SELECTOR, ".card")
    Cart_Buttons = (By.CSS_SELECTOR, ".btn-custom")

    #---ACTIONS----
    @allure.step("Adding product '{product_name}' to cart")
    def add_product_to_cart(self, product_name):

        self.wait.until(EC.presence_of_element_located(self.Product_Cards))
        products = self.driver.find_elements(*self.Product_Cards)

        for product in products:
            name = product.find_element(By.CSS_SELECTOR, "b").text

            if product_name in name:

                buttons = product.find_elements(By.TAG_NAME, "button")

                for button in buttons:
                    if button.text.strip() == "Add To Cart":
                        button.click()
                        return

    def go_to_cart(self):
        self.driver.execute_script("window.scrollTo(0,0);")
        self.wait.until(EC.presence_of_element_located(self.Cart_Buttons))
        buttons = self.driver.find_elements(*self.Cart_Buttons)
        for button in buttons:
            if button.text.strip() == "Cart":
                button.click()
