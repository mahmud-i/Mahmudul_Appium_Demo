from pages.base_page import BasePage
import allure

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.counter_plus_button = (self.xpath_locator, "//*[@content-desc='counter plus button']")
        self.add_to_cart_button = (self.xpath_locator, "//*[@content-desc='Add To Cart button']")
        self.cart_badge = (self.xpath_locator, "//*[@content-desc='cart badge']")

    @allure.step("Click on Counter Plus Button")
    def click_on_counter_plus_button(self):
        self.click(*self.counter_plus_button)
        return self

    @allure.step("Click on Add to Cart Button")
    def click_on_add_to_cart_button(self):
        self.click(*self.add_to_cart_button)
        return self

    @allure.step("Click on Cart Badge")
    def click_on_cart_badge(self):
        self.click(*self.cart_badge)