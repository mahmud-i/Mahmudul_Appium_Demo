from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.email_locator = (self.accessibility_id_locator, "Username input field")
        self.password_locator = (self.accessibility_id_locator, "Password input field")
        self.login_button_locator = (self.accessibility_id_locator, "Login button")

    @allure.step("Login with Valid Email and Password")
    def login_with_valid_email_and_password(self, email, password):
        self.enter_text(*self.email_locator, email)
        self.enter_text(*self.password_locator, password)
        self.click(*self.login_button_locator)