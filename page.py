from locator import *
from element import BasePageElement, CheckXpath
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

# class CheckXpathElement(BasePageElement):
#     locator = "/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]"

# class checkDashboard(CheckXpath):
#     value=""
def is_element_found(driver, xpath):
    try:
        return WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except NoSuchElementException:
        # If the element was not found, print an error message
        print(f"Error: Element with XPath '{xpath}' not found on page")
    finally:
        # If the element was found, print a success message
        print(f"Success: Element with XPath '{xpath}' found on page")

def navigate_and_access(driver, xpath):
    actions = ActionChains(driver)
    actions.move_by_offset(268, 316).perform()
    print("Move to inner scrollbar")
    time.sleep(10)
    try:
        elementExampleButton = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", elementExampleButton)
        elementExampleButton.click()
    except NoSuchElementException:
        print(f"Error: Element with XPath '{xpath}' not found on page")
        
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
class ExamplePage(BasePage):
    def navigate_and_access_example(self):
        xpath = "/html/body/div[2]/div/div[1]/div/div/div/section/div[55]/a"
        navigate_and_access(self.driver, xpath)
        
    def is_example_sidebar_found(self):
        example_button = "/html/body/div[2]/div/div[1]/div/div/div/section/div[55]/a"
        is_element_found(self.driver, example_button)
        
    def is_pill_active(self):
        active_example_button = "/html/body/div[9]/div/div[1]/div/div/div/section/div[55]/a"
        is_element_found(self.driver, active_example_button)
    def is_add_btn_found(self):
        active_example_button = "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/button"
        is_element_found(self.driver, active_example_button)
