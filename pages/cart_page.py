from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.proceed_to_checkout_button = (self.xpath_locator, "//*[@content-desc='Proceed To Checkout button']")

    @allure.step("Click on Proceed to Checkout Button")
    def click_on_proceed_to_checkout_button(self):
        self.click(*self.proceed_to_checkout_button)