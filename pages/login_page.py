from selenium.webdriver.common.by import By
from utils.config_reader import get_base_url


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def load(self):
        self.driver.get(get_base_url())

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()