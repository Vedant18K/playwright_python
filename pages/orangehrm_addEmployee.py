from playwright.sync_api import Page

class AddEmployee:
    def __init__(self,page:Page):
        self.page = page
        self.PIM = page.get_by_role("link", name="PIM")
        self.add_button = page.get_by_role("button", name=" Add")
        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.middle_name_input = page.get_by_role("textbox", name="Middle Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")
        self.emp_id = page.get_by_role("textbox").nth(4)
        self.save_button = page.get_by_role("button", name="Save")
        
    def add_employee_test(self):
        self.PIM.click()
        self.add_button.click()
        self.first_name_input.fill("First ")
        self.middle_name_input.fill("Middle")
        self.last_name_input.fill("Last")
        self.emp_id.fill("00002")
        self.save_button.click()