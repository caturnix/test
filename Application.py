from selenium import webdriver
import re
import time
import datetime
import random
import pytest
import postgresql
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import allure
from allure_commons.types import AttachmentType

url = "https://qa.sberbank-partner.ru"
passport = str(random.randrange(1000000000, 1999999999))



class Application:
    def __init__(self):
        #self.binary = FirefoxBinary('/Users/vvperepelkin/desktop/Firefox.app/Contents/MacOS/firefox')
        #self.wd = webdriver.Firefox(firefox_binary=self.binary)
        self.wd = webdriver.Chrome()
        self.wd.delete_all_cookies()
        self.wd.maximize_window()
        self.wait = WebDriverWait(self.wd, 60)

    def generate_phone(self):
        generatedphone = random.randrange(1000000, 9999999)
        client_phone = str('102' + str(generatedphone))
        return client_phone

    @allure.step('Открытие страницы логина')
    def open_login_page(self):
        wd = self.wd
        self.wait_overlay()
        wd.get(url)
    
    @allure.step('Авторизация')
    def login(self, user, password):
        # авторизация
        wd = self.wd
        wd.delete_all_cookies()
        wd.find_element_by_name('username').send_keys(user)
        wd.find_element_by_name('password').send_keys(password)
        time.sleep(2)
        wd.find_element_by_class_name('default').click()
        print("Осуществлен вход под " + user)
