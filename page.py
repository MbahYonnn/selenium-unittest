from locator import *
from selenium import webdriver
from element import BasePageElement, CheckXpath
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
import time

# class CheckXpathElement(BasePageElement):
#     locator = "/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]"

# class checkDashboard(CheckXpath):
#     value=""

def is_element_found(driver, xpath, variable):
    try:
        return WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except NoSuchElementException:
        # If the element was not found, print an error message
        print(f"Error: Element {variable} : '{xpath}' not found on page")
    finally:
        # If the element was found, print a success message
        print(f"Success: Element {variable} :  '{xpath}' found on page")

def navigate_and_access(driver, xpath):
    actions = ActionChains(driver)
    actions.move_by_offset(268, 316).perform()
    print("Move to inner scrollbar")
    time.sleep(2)
    try:
        elementExampleButton = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", elementExampleButton)
        elementExampleButton.click()
    except NoSuchElementException:
        print(f"Error: Element with XPath '{xpath}' not found on page")   

def get_element_color(driver, xpath):
    element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    rgb = element.value_of_css_property('background-color')
    hex_color = Color.from_string(rgb).hex
    return hex_color

def assert_color(driver, xpath, expected_color):
    # Access the element and get its color
    hex = get_element_color(driver, xpath)
    # Assertion
    assert hex is not None, f"Error: Color assertion failed due to element not found for XPath: {xpath}"
    assert hex == expected_color, f"Error: The element's color '{hex}' does not match the expected color '{expected_color}'."
    # Print message if the color is found and matches the expected color
    print(f"The element's color is as expected: {hex}")
    return hex

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
        xpath = "/html/body/div[2]/div/div[1]/div/div/div/section/div[56]/a"
        navigate_and_access(self.driver, xpath)
        
    def is_example_sidebar_found(self):
        example_button = "/html/body/div[2]/div/div[1]/div/div/div/section/div[56]/a"
        is_element_found(self.driver, example_button, 'example_button')
        
    def is_pill_active(self):
        active_example_button = "/html/body/div[9]/div/div[1]/div/div/div/section/div[56]/a"
        is_element_found(self.driver, active_example_button, 'active_example_button')
    def is_add_btn_found(self):
        active_example_button = "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/button"
        is_element_found(self.driver, active_example_button, 'active_example_button')
    def is_index_breadcrumb_found(self):
        home_breadcrumb = ("/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div/span")
        chevron_1 = ("/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[1]")
        breadcrumb_1 = ("/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[1]/li/span[1]/span")
        chevron_2 = ("/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[1]/li/span[2]")
        breadcrumb_2 = ("/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[2]")
        elements_to_check = [
            (home_breadcrumb, "Home Breadcrumb"),
            (chevron_1, "Chevron 1"),
            (breadcrumb_1, "Breadcrumb 1"),
            (chevron_2, "Chevron 2"),
            (breadcrumb_2, "Breadcrumb 2")
            # Add more XPaths and variable names as needed
        ]
        for xpath, variable in elements_to_check:
            element = is_element_found(self.driver, xpath, variable)
            if element is None:
                print(f"Error: Element {variable} : '{xpath}' not found on page")
            else:
                # Perform assertions or other actions based on the element's presence
                # For example:
                assert element.is_displayed(), f"Error: Element {variable} : '{xpath}' not displayed on page"        
    def check_filter_button(self):
        btn_filter = "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[7]/div[2]/button[2]"
        is_element_found(self.driver,btn_filter,btn_filter)
    def check_color_button(self):
        # Define the XPath of the element whose color you want to assert
        btn_filter = "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[7]/div[2]/button[2]"
        expected_color = "#7367f0"
        # Assert the element's hex color
        rgb = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, btn_filter))).value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        # actual_color = get_element_hex_color(self.driver, expected_color)
        # Assertion
        assert hex is not None, "Error: Color assertion failed due to element not found."
        assert hex == expected_color, f"Error: The element's color '{hex}' does not match the expected color '{expected_color}'."
    def checkss(self):
        ## Define the XPath of the element you want to test
        btn_filter_xpath = "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[7]/div[2]/button[2]"
        expected_color = "#7367f0"
        # Access the element and get its color using the function
        hex = assert_color(self.driver, btn_filter_xpath, expected_color)
        hex