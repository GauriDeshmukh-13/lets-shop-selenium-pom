from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #---LOCATORS----
    items = (By.CSS_SELECTOR, ".items")
    buttons = (By.TAG_NAME, "button")

    def get_cart_product_names(self):
        self.wait.until(EC.presence_of_all_elements_located(self.items))
        products_in_cart = self.driver.find_elements(*self.items)

        product_names = []
        for product in products_in_cart:
            product_names.append(product.find_element(By.TAG_NAME, "h3").text)

        return product_names
