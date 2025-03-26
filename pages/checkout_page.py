from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.full_name = (self.accessibility_id_locator, "Full Name* input field")
        self.address_line = (self.accessibility_id_locator, "Address Line 1* input field")
        self.address_line2 = (self.accessibility_id_locator, "Address Line 2 input field")
        self.city = (self.accessibility_id_locator, "City* input field")
        self.state = (self.accessibility_id_locator, "State/Region input field")
        self.zip_code = (self.accessibility_id_locator, "Zip Code* input field")
        self.country = (self.accessibility_id_locator, "Country* input field")
        self.payment_button = (self.xpath_locator, "//*[@content-desc='To Payment button']")

    @allure.step("Fill Checkout Information")
    def fill_checkout_information(self, full_name, address_line, address_line2, city, state, zip_code, country):
        self.enter_text(*self.full_name, full_name)
        self.enter_text(*self.address_line, address_line)
        self.enter_text(*self.address_line2, address_line2)
        self.enter_text(*self.city, city)
        self.enter_text(*self.state, state)
        self.enter_text(*self.zip_code, zip_code)
        self.enter_text(*self.country, country)
        self.click(*self.payment_button)