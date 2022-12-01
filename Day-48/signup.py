from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")


first_name.send_keys("seon yeong")
last_name.send_keys("fang")
email.send_keys("siss9898@naver.com")

sign_up = driver.find_element(By.CLASS_NAME,"btn")
sign_up.send_keys(Keys.ENTER)