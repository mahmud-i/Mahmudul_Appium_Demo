import pytest
import json
import os
import shutil
import configparser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.product_page import ProductPage
from pages.payment_page import PaymentPage
from pages.review_order_page import ReviewOrderPage


def clear_directory(directory):
    """Clear the contents of the given directory."""
    if os.path.exists(directory):
        # Remove all files and subdirectories in the directory
        shutil.rmtree(directory)
    os.makedirs(directory)


def pytest_sessionstart(session):
    """Clear directories before the test session starts."""

    # Clear previous allure-results and allure-report directories
    clear_directory("reports/allure-results")
    clear_directory("reports/allure-report")


@pytest.fixture(scope="session")
def test_data():
    """Load test data from JSON file."""
    with open('resources/test_data.json') as f:
        data = json.load(f)
    return data


# # fixture to start and stop the Appium server
# @pytest.fixture(scope="session")
# def appium_server():
#     # Start the Appium server process
#     appium_process = subprocess.Popen("appium", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     time.sleep(5)  # wait for some time to start the server
#     print("Appium server started")
#
#     yield appium_process  # Yield the server process to the test
#
#     # Stop the Appium server after the test session completes
#     appium_process.terminate()
#     print("Appium server stopped")


# Setup fixture for Appium driver
@pytest.fixture(scope="class")
def setup(request):
    """Setup Appium driver and initialize page objects directly from config.ini."""

    # Read the config file
    config = configparser.ConfigParser()
    config.read("resources/config.ini")

    # Create appium options
    capabilities = UiAutomator2Options()

    # Extract values from the config file and assign them to the capabilities
    capabilities.platformName = config.get("Appium", "platformName")
    capabilities.device_name = config.get("Appium", "deviceName")
    capabilities.automation_name = config.get("Appium", "automationName")
    capabilities.app_package = config.get("Appium", "appPackage")
    capabilities.app_activity = config.get("Appium", "appActivity")
    capabilities.app = config.get("Appium", "apkPath")    # APK file path
    capabilities.udid = config.get("Appium", "deviceID")  # Android device ID
    capabilities.no_reset = True   # Prevents reinstalling the app every time

    # Get the Appium server URL
    appium_server_url = config.get("Appium", "appiumServerURL")



    # Create the Appium driver
    driver = webdriver.Remote(appium_server_url, options = capabilities)
    driver.implicitly_wait(5)

    # Initialize page objects
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.home_page = HomePage(driver)
    request.cls.cart_page = CartPage(driver)
    request.cls.checkout_page = CheckoutPage(driver)
    request.cls.checkout_complete_page = CheckoutCompletePage(driver)
    request.cls.product_page = ProductPage(driver)
    request.cls.payment_page = PaymentPage(driver)
    request.cls.review_order_page = ReviewOrderPage(driver)

    yield driver    # yield the driver to the test

    driver.quit()   # Close the Appium driver


def pytest_sessionfinish(session, exitstatus):
    """Generate Allure reports automatically after test run"""
    # Generate Allure report
    os.system("allure generate reports/allure-results -o reports/allure-report --clean")
