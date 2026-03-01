from playwright.sync_api import expect
from .base import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK = '//button[@data-test="add-to-cart-sauce-labs-backpack"]'
    CART_LINK = '.shopping_cart_link'

    def add_backpack_to_cart(self):
        expect(self.page.locator(self.ADD_BACKPACK)).to_be_enabled()
        self.page.click(self.ADD_BACKPACK)
        self.page.click(self.CART_LINK)
