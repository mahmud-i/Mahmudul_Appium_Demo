import pytest
import allure

@pytest.mark.usefixtures("setup", "test_data")
class TestDemoApp:

    @allure.description(
        "Given user opens the Sauce Labs mobile application\n"
        "When they click on Menu\n"
        "And click on Login\n"
        "And login with Valid Email & Password\n"
        "And choose a Product\n"
        "And click on counter Plus Button\n"
        "And click on Add To Cart button\n"
        "And click on Cart Badge\n"
        "And click on Proceed To Checkout Button\n"
        "And fill Checkout Information\n"
        "And fill Payment Information\n"
        "And click on Place Order button\n"
        "And click on Continue Shopping button\n"
        "Then user should return to Home screen"
    )


    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    def test_checkout_order(self, test_data):

        login_data = test_data["login"]
        checkout_data = test_data["checkout"]
        payment_data = test_data["payment"]

        # Step 1: Open Menu and Login
        self.home_page.click_on_open_menu()
        self.home_page.click_on_login_button()

        email = login_data["email"]
        password = login_data["password"]
        self.login_page.login_with_valid_email_and_password(email, password)

        self.take_screenshot("Login Successful")

        # Step 2: Choose Product
        self.home_page.click_on_product1()
        self.product_page.click_on_counter_plus_button()
        self.product_page.click_on_add_to_cart_button()

        self.take_screenshot("Product Added to Cart")

        # Step 3: View Cart and Proceed to Checkout
        self.product_page.click_on_cart_badge()
        self.cart_page.click_on_proceed_to_checkout_button()

        self.take_screenshot("Proceed to Checkout")

        # Step 4: Fill Checkout Information
        checkout = checkout_data.copy()

        self.checkout_page.fill_checkout_information(**checkout)

        self.take_screenshot("Checkout Information Filled")

        # Step 5: Fill Payment Information
        payment =  payment_data.copy()

        self.payment_page.fill_payment_information(**payment)

        self.take_screenshot("Payment Information Filled")

        # Step 6: Review Order
        self.payment_page.click_on_review_order_button()

        self.take_screenshot("Review Order")

        # Step 7: Place Order
        self.review_order_page.click_on_place_order_button()

        self.take_screenshot("Place Order")

        # Step 8: Continue Shopping
        self.checkout_complete_page.click_on_continue_shopping_button()

        self.take_screenshot("Returned to Home")

        # Step 9: Verify
        product_text = self.home_page.get_products_text()
        assert product_text == "Products", f"Expected 'Products' but got {product_text}"



    @allure.step("Take a screenshot and attach it to Allure report")
    def take_screenshot(self, step_name):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=step_name, attachment_type=allure.attachment_type.PNG)
