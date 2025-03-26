from pages.base_page import BasePage
import allure

class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.full_name = (self.xpath_locator, "//android.widget.EditText[@content-desc='Full Name* input field']")
        self.card_number = (self.accessibility_id_locator, "Card Number* input field")
        self.expiration_date = (self.accessibility_id_locator, "Expiration Date* input field")
        self.security_code = (self.accessibility_id_locator, "Security Code* input field")
        self.review_order_button = (self.xpath_locator, "//*[@content-desc='Review Order button']")

    @allure.step("Fill Payment Information")
    def fill_payment_information(self, full_name, card_number, expiration_date, security_code):
        self.enter_text(*self.full_name, full_name)
        self.enter_text(*self.card_number, card_number)
        self.enter_text(*self.expiration_date, expiration_date)
        self.enter_text(*self.security_code, security_code)


    @allure.step("Click on Review Order Button")
    def click_on_review_order_button(self):
        self.click(*self.review_order_button)