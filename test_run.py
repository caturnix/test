import time
from Application import Application
import Application
import allure

@allure.testcase('РЦИК создает сделку')
def test_create_deal(app):
        app.open_login_page()
        app.login('abc@gmail.com', 'password')
        app.logout()