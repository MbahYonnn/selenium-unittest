import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import page
import time
import testcase.supervisionalbe

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("user-data-dir=/Users/macintosh/Library/Caches/Google/Chrome/Default")
        # self.options.add_argument("headless")
        # self.options.add_argument("window-size=1920,1080")
        # self.options.add_argument('ignore-certificate-errors')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://backoffice-acasia-dev.ainosi.com")
        loginPage = page.LandingPage(self.driver)
        # assert loginPage.is_title_matches()
        loginPage.input_username()
        loginPage.input_password()
        loginPage.click_login_button()

    def test_add_supervisionalBE_byExcel(self):
        pages = testcase.supervisionalbe.SupervisionalPage(self.driver)
        pages.headerSidebar()
        pages.navigate_and_access_SuperBE()
        pages.excelSVBE()
        pages.navigate_and_submit_form()
        time.sleep(2)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    # HTMLTestRunner.main()



# ++++++++++++++++ Tutorial test search ++++++++++++++++++
    # def test_search_python(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.is_title_matches()
    #     mainPage.search_text_element = "pycon"
    #     mainPage.click_go_button()
    #     search_result_page = page.SearchResultPage(self.driver)
    #     assert search_result_page.is_results_found()
    # ++++++++++++++++ Tutorial test search ++++++++++++++++++
# def test_assert_headersidebar(self):
    #     dashboardPage = page.DashboardPage(self.driver)
    #     dashboardPage.is_sidebar_found()
    #     time.sleep(3)