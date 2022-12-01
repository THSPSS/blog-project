from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# articles.click()


Community_portal = driver.find_element(By.LINK_TEXT,"Community portal")
# Community_portal.click()

search = driver.find_element(By.NAME,"search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

