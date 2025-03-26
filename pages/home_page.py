from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.open_menu_locator = (self.xpath_locator,"//*[@content-desc='open menu']")
        self.login_button_locator = (self.accessibility_id_locator,"menu item log in")
        self.product1_locator = (self.xpath_locator,"(//*[@content-desc='store item'])[1]")
        self.product_text = (self.xpath_locator,"//*[@text='Products']")

    @allure.step("Click on Open Menu")
    def click_on_open_menu(self):
        self.click(*self.open_menu_locator)
        return self

    @allure.step("Click on Login Button")
    def click_on_login_button(self):
        self.click(*self.login_button_locator)


    @allure.step("Click on Product 1")
    def click_on_product1(self):
        self.click(*self.product1_locator)


    @allure.step("get header text")
    def get_products_text(self):
        return self.get_text(*self.product_text)