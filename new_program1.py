print("Branch")
driver.find_element(By.XPATH,"//a[contains(text(),'Alert with Textbox') ]").click()
driver.find_element(By.XPATH,"//button[text()='click the button to demonstrate the prompt box ']").click()
alert=driver.switch_to.alert
time.sleep(2)