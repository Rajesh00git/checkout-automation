from .base import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = '[data-test="checkout"]'

    def go_to_checkout(self):
        self.page.click(self.CHECKOUT_BTN)
