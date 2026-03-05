from pages.orangehrm_login_page import LoginPage
from fixtures.userData import userinfo

def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate() 
    login_page.login(userinfo.username, userinfo.password)  
    
def test_invalid_login(page):
    login_page =LoginPage(page)