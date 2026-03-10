from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_addUser import AddUser
from fixtures.userData import userinfo

def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate() 
    login_page.login(userinfo.username, userinfo.password)
    
def test_add_user(page):
    login_page = LoginPage(page)
    login_page.navigate() 
    login_page.login(userinfo.username, userinfo.password)
    add_user = AddUser(page)
    add_user.add_user_test()
    