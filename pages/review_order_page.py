from pages.base_page import BasePage
import allure

class ReviewOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.place_order_button = (self.xpath_locator, "//*[@content-desc='Place Order button']")

    @allure.step("Click on Place Order Button")
    def click_on_place_order_button(self):
        self.click(*self.place_order_button)