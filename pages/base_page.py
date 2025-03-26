from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.xpath_locator = AppiumBy.XPATH
        self.accessibility_id_locator = AppiumBy.ACCESSIBILITY_ID

    def click(self, locator_type,locator):
        self.driver.find_element(locator_type, locator).click()
        self.driver.implicitly_wait(5)

    def enter_text(self, locator_type, locator, text):
        self.driver.find_element(locator_type, locator).clear()
        self.driver.find_element(locator_type, locator).send_keys(text)

    def get_text(self, locator_type, locator):
        return self.driver.find_element(locator_type,locator).text
