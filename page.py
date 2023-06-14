from locator import *
from element import BasePageElement, CheckXpath
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# class CheckXpathElement(BasePageElement):
#     locator = "/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]"

# class checkDashboard(CheckXpath):
#     value=""

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        
class LandingPage(BasePage):
    
    # search_text_element = SearchTextElement()
    def is_title_matches(self):
        try:
            return "Acasia" in self.driver.title
        finally:
            print("Page is ", self.driver.title)
    def input_username(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='Username']"))).send_keys("Leon_acasia_dev")
                # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]")))
    
    def input_password(self):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.send_keys("Aino2022")
    
    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()
    
class DashboardPage(BasePage):
    
    # founds = checkDashboard()
    def is_sidebar_found(self):                    
        try:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]")))
        except NoSuchElementException:
            # If the element was not found, print an error message
            print("Error: Element not found on page")
        finally:
            # If the element was found, print a success message
            print("Success: Element found on page")

    
