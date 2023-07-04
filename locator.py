# from operator import imod
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    # USERNAME_FIELD = (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/input")
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[name='Username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class='vs-component vs-button vs-button-primary vs-button-filled']")
    
class DashboardLocators(object):
    HEADER_SIDEBAR = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]")
    
class TemplateLocators(object):
    HEADER_SIDEBAR = (By.XPATH, "/html/body/div[18]/div/div[1]/div/div/div/section/span[12]")
    BUTTON_EXAMPLE = (By.XPATH, "/html/body/div[18]/div/div[1]/div/div/div/section/div[55]/a")
    BUTTON_EXAMPLE_PILL_ACTIVE = (By.XPATH, "/html/body/div[9]/div/div[1]/div/div/div/section/div[55]/a")
    TITLE_EXAMPLE = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[1]/h2")
    BUTTON_HOME = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div/span/svg")
    CHEVRON_1 = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/span/span/svg")
    BREADCRUMB_1 = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[1]/li/span[1]/span")
    CHEVRON_2 = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[1]/li/span[2]/span/svg")
    BREADCRUMB_2 = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[2]/span")
    FN_FILTER_INPUT_TEXT = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[1]/span")
    FN_FILTER_INPUT_NUMBER = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/span")
    FN_FILTER_DD_SELECT = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[1]/span")
    FN_FILTER_RANGE_DATE = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[4]/div[1]/span")
    FN_FILTER_DD_WITH_LIMIT_RANGER = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[6]/div[1]/span")
    BUTTON_FILTER = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[7]/div[2]/button[2]")
    BUTTON_RESET = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[7]/div[2]/button[1]")
    BUTTON_ADD = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/button")
    BUTTON_DD_NUMBER_PAGINATION = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/button")
    HEADER_NUMBER = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/div[1]")
    HEADER_ONE = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]")
    HEADER_TWO = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/div[3]")
    HEADER_ACTIONS = (By.XPATH, "/html/body/div[9]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[3]/div/div")
    TITLE_ADD = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[1]/h2")
    ADD_PAGE_BUTTON_HOME = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div/span/svg")
    ADD_PAGE_CHEVRON_1 = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/span/span/svg")
    ADD_PAGE_BREADCRUMB_1 = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[1]/li/span[1]/span")
    ADD_PAGE_CHEVRON_2 = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[1]/li/span[2]/span/svg")
    ADD_PAGE_BREADCRUMB_2 = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[2]/li/a")
    ADD_PAGE_CHEVRON_3 = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/div[2]/li/span/span/svg")
    ADD_PAGE_BREADCRUMB_3 = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/ul/li[2]/span")
    ADD_PAGE_CARD_TITLE_1 = (By.XPATH, "/html/body/div[2]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div[1]/h4")
    
    
    

    