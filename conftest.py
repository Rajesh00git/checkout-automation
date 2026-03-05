import os
import pytest
import sys
sys.path.append('.')

from playwright.sync_api import sync_playwright
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="function", params=["chromium", "firefox"])
def page(request):
    headless_env = os.getenv("HEADLESS", "false").lower() == "true"

    with sync_playwright() as p:
        browser = p[request.param].launch(
            headless=headless_env,
            slow_mo=0 if headless_env else 500
        )
        context = browser.new_context()
        _page = context.new_page()
        yield _page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def logged_in_pages(page):
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)
    return {
        "inventory": InventoryPage(page),
        "cart": CartPage(page),
        "checkout": CheckoutPage(page)
    }
