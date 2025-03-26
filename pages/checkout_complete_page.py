from pages.base_page import BasePage
import allure

class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.continue_shopping_button = (self.xpath_locator, "//*[@content-desc='Continue Shopping button']")

    @allure.step("Click on Continue Shopping Button")
    def click_on_continue_shopping_button(self):
        self.click(*self.continue_shopping_button)