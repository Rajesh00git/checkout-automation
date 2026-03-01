from .base import BasePage

class LoginPage(BasePage):
    USER_INPUT = '[data-test="username"]'
    PASS_INPUT = '[data-test="password"]'
    LOGIN_BTN = '[data-test="login-button"]'

    def login(self, user, pwd):
        self.page.fill(self.USER_INPUT, user)
        self.page.fill(self.PASS_INPUT, pwd)
        self.page.click(self.LOGIN_BTN)
