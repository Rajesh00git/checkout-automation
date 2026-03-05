from playwright.sync_api import expect
from .base import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = '[data-test="firstName"]'
    LAST_NAME = '[data-test="lastName"]'
    ZIP_CODE = '[data-test="postalCode"]'
    CONTINUE_BTN = '[data-test="continue"]'
    FINISH_BTN = '[data-test="finish"]'
    COMPLETE_MSG = '[data-test="complete-header"]'
    COMPLETE_TEXT = '[data-test="complete-text"]'

    def complete_checkout_cod(self):
        # Fill checkout details
        self.page.fill(self.FIRST_NAME, "Test")
        self.page.fill(self.LAST_NAME, "User")
        self.page.fill(self.ZIP_CODE, "75001")
        self.page.click(self.CONTINUE_BTN)

        # Click finish on overview page
        self.page.click(self.FINISH_BTN)

        # Wait for confirmation message
        complete_locator = self.page.locator(self.COMPLETE_MSG)
        expect(complete_locator).to_be_visible(timeout=10000)

        # Get confirmation text
        msg = complete_locator.inner_text()
        return "Thank you for your order!" in msg
    
    def get_confirmation_text(self):
        """Helper to get full confirmation message"""
        return self.page.locator(self.COMPLETE_TEXT).inner_text()
