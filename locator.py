# from operator import imod
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    # USERNAME_FIELD = (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/input")
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[name='Username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class='vs-component vs-button vs-button-primary vs-button-filled']")
    
class DashboardLocators(object):
    HEADER_SIDEBAR = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]")
