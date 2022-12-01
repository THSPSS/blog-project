from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as excp
import time

ACCOUNT_EMAIL = "sunyeongbang98@gmail.com"
ACCOUNT_PASSWORD = "MQjWh.)&jD65z+8"



chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3299474513&distance=25.0&geoId=105149562&keywords=python%20developer")
driver.maximize_window()

time.sleep(2)


log_in = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]").click()

user_name = driver.find_element(By.ID,"username").send_keys(ACCOUNT_EMAIL)

user_password = driver.find_element(By.ID,"password")
user_password.send_keys(ACCOUNT_PASSWORD)
user_password.send_keys(Keys.ENTER)



roll_down = driver.find_element(By.ID,"ember166")
roll_down.click()

jobs = driver.find_elements(By.CSS_SELECTOR,".scaffold-layout__list-container li")
jobs_ids = [value.get_attribute("id") for value in jobs]


for id in jobs_ids:
    if id != '':
        job_id = driver.find_element(By.ID,id)
        job_id.click()
        time.sleep(3)
        save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save.click()
        time.sleep(10)
        # follow = driver.find_element(By.CLASS_NAME, "follow")




