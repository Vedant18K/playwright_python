from playwright.sync_api import Page

class LoginPage:
    LOGIN_URL = "/web/index.php/auth/login"

    def __init__(self, page: Page):
        self.page = page  
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_btn = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto(self.LOGIN_URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()