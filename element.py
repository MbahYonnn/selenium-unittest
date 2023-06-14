# from lib2to3.pgen2 import driver
# from optparse import Values
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement(object):
    def __set__(self,obj,value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH,self.locator))
        driver.find_element(By.XPATH,self.locator).clear()
        driver.find_element(By.XPATH,self.locator).send_keys(value)
    def __get__(self,obj,owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH,self.locator))
        element = driver.find_element(By.XPATH,self.locator)
        return element.get_attribute("value")

class CheckXpath(object):
    def __set__(self,obj,value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH,self.value))
        print(f"{self.value} found!")