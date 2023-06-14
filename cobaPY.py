import time
from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")
# .options.add_argument("headless")
# .options.add_argument("window-size=1920,1080")
# .options.add_argument('ignore-certificate-errors')
options.add_argument(
    "user-data-dir=/Users/macintosh/Library/Caches/Google/Chrome/Default/Cache/Cache_Data")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
# .driver.implicitly_wait(10)
driver.get("https://backoffice-acasia-dev.ainosi.com")
time.sleep(10)
username_login = "/html/body/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/input"
password_login = "/html/body/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[4]/div/div/input"
driver.find_element(By.XPATH, username_login).send_keys("Leon_acasia_dev")
element_password = driver.find_element(By.XPATH, password_login)
element_password.send_keys("Aino2022")
element_password.send_keys(Keys.RETURN)
print("Login Berhasil")
time.sleep(10)
try:
    assert WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div[1]")))
finally:
    print("Berhasil menemukan Logo kiri atas")

# Get the current window size
actions = ActionChains(driver)
actions.move_by_offset(268, 316).perform()
print("move to inner scrollbar")
scrollable_element = driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/section/div[149]")
elementSuperBE = driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/section/div[45]/a")
driver.execute_script("arguments[0].scrollIntoView();", elementSuperBE)
elementSuperBE.click()


time.sleep(5)
# WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, target_xpath))).click()
# Continue with other actions on the page


# 290 281
# class SupervisionalPage:
#     def excelSVBE():
#         wb = load_workbook(
#             filename="/Users/macintosh/Documents/SeleUnit/data_supervisional_be.xlsx")
#         sheetRange = wb['Sheet1']
#         i = 2
#         while i <= len(sheetRange['A']):
#             legal_name = sheetRange['C' + str(i)].value
#             brand_name = sheetRange['D' + str(i)].value
#             phone = sheetRange['E' + str(i)].value
#             email = sheetRange['F' + str(i)].value
#             web_address = sheetRange['G' + str(i)].value
#             address = sheetRange['H' + str(i)].value
#             tax_code = sheetRange['I' + str(i)].value
#             username = sheetRange['J' + str(i)].value
#             password = sheetRange['K' + str(i)].value
#             yield legal_name, brand_name, phone, email, web_address, address, tax_code, username, password
#             i += 1

#     def form():
#         for values in .excelSVBE():
#             legal_name, brand_name, phone, email, web_address, address, tax_code, username, password = values
#             # Do something with the values
#             print("Legal Name:", legal_name)
#             print("Brand Name:", brand_name)
#             print("Phone:", phone)
#             print("Email:", email)
#             print("Web Address:", web_address)
#             print("Address:", address)
#             print("Tax Code:", tax_code)
#             print("Username:", username)
#             print("Password:", password)
#             print("------------")


# page = SupervisionalPage()
# page.form()
