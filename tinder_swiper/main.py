from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://tinder.com/app/recs")
driver.maximize_window()

time.sleep(4)

login = driver.find_element(By.XPATH,'//*[@id="q-1380955487"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]').click()
time.sleep(5)
phone_number = driver.find_element(By.XPATH,'//*[@id="q1185630733"]/main/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]').click()
time.sleep(5)

put_pn = driver.find_element(By.NAME,"phone_number")
time.sleep(1)
put_pn.send_keys("01023097903")
put_pn.send_keys(Keys.ENTER)

time.sleep(30)
sending_email = driver.find_element(By.XPATH,'//*[@id="q1185630733"]/main/div/div/div[1]/div/div[2]/button/div[2]').click()

accept_1 = driver.find_element(By.XPATH,'//*[@id="q1185630733"]/main/div/div/div/div[3]/button[1]').click()

accept_2 = driver.find_element(By.XPATH,'//*[@id="q1185630733"]/main/div/div/div/div[3]/button[2]').click()

# try:
#     move_to_left = driver.find_element(By.XPATH,'//*[@id="q-1380955487"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]')
#     move_to_left.click()
# except NoSuchElementException:
#     time.sleep(4)
#     move_to_left.click()
# except ElementClickInterceptedException:
#     back_to_tinder = driver.find_element(By.LINK_TEXT,"BACK TO TINDER").click()
#     move_to_left.click()
#
