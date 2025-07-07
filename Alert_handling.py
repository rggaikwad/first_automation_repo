import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
# new changes
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service=Service("C:/Users/rushi/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=service,options=options)
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
time.sleep(2)

# alert with ok

# driver.find_element(By.XPATH,"//button[contains(text(),'click the button to display an  alert box')]").click()
# alert=driver.switch_to.alert
# alert.accept()


# alert with OK and cancel
# driver.find_element(By.XPATH,"//a[text()='Alert with OK & Cancel ']").click()
# # wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='click the button to display a confirm box ']")))
# ele=driver.find_element(By.XPATH,"//button[text()='click the button to display a confirm box ']")
# # driver.execute_script("arguments[0].click();",ele)-another_way
# alert=driver.switch_to.alert
# alert.dismiss()

# alert with textbox value

driver.find_element(By.XPATH,"//a[contains(text(),'Alert with Textbox') ]").click()
driver.find_element(By.XPATH,"//button[text()='click the button to demonstrate the prompt box ']").click()
alert=driver.switch_to.alert
time.sleep(2)
alert.send_keys('rushikesh')

print("File changed by Manju!!!")

time.sleep(3)
time.sleep(1)


print("changed")

print("Mahesh")

