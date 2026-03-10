from playwright.sync_api import Page

class AddUser:
    def __init__(self,page:Page):
        self.page = page
        self.admin_role = page.get_by_role("link", name="Admin")
        self.add_user = page.get_by_role("button", name=" Add")
        self.select_role = page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").nth(0)
        self.select_option_admin = page.get_by_role("option", name="Admin")
        self.enter_name = page.get_by_role("textbox", name="Type for hints...")
        self.select_employee_name = page.get_by_text("Radha")
        self.select_status = page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").nth(1)
        self.selct_status_option =page.get_by_role("option", name="Enabled")
        self.username_input=page.get_by_role("textbox").nth(2)
        self.password_input=page.get_by_role("textbox").nth(3)
        self.comfirm_password_input = page.get_by_role("textbox").nth(4)
        self.save_button = page.get_by_role("button", name="Save")
        
    def add_user_test(self):
        self.admin_role.click()
        self.add_user.click()
        self.select_role.click()
        self.select_option_admin.click()
        self.enter_name.fill("Radha")
        self.select_employee_name.click()
        self.select_status.click()
        self.selct_status_option.click()
        self.username_input.fill("testing")
        self.password_input.fill("Admin@1234")
        self.comfirm_password_input.fill("Admin@1234")
        self.save_button.click()
        