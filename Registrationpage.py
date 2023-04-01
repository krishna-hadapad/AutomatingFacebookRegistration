from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\Krishna C Hadapad\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

date = "15"
Month = "May"
year = "1997"

driver.get(r"https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Create new account").click()

#Adding Text to Input fields
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Krishna")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Hadapad")
driver.find_element(By.XPATH,"//input[@name='reg_email__']").send_keys("9886145745")
driver.find_element(By.XPATH,"//input[@name='reg_passwd__']").send_keys("Krishna@1997")
driver.find_element(By.XPATH,"//input[@value='2']").click()


# For selecting Date pickers
Dates = driver.find_elements(By.XPATH,"//select[@id='day']/option")
print("Number of dates", len(Dates))

driver.find_element(By.XPATH,"//select[@id='day']/option").click()

for D in Dates:
    if D.text == date:
        D.click()

Months = driver.find_elements(By.XPATH,"//select[@id='month']/option")
print("Number of Months", len(Months))

driver.find_element(By.XPATH,"//select[@id='month']/option").click()

for M in Months:
    if M.text == Month:
        M.click()

Years = driver.find_elements(By.XPATH,"//select[@id='year']/option")
print("Number of years", len(Years))

driver.find_element(By.XPATH,"//select[@id='year']/option").click()

for Y in Years:
    if Y.text == year:
        Y.click()

driver.quit()
