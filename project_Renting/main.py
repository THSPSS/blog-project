import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time



CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"




ZILLOW = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
} #for not getting CAPTCHA


response = requests.get(ZILLOW,headers=headers)
zillow_text = response.text
first_part="https://www.zillow.com"

soup = BeautifulSoup(zillow_text,"lxml")



prices = soup.find_all(class_="hRqIYX")
price_list = [price.get_text().split(" ")[0] for price in prices]

addresses = soup.find_all(class_="lhIXlm")
address_list = [address.get_text() for address in addresses]

links = [div.find('a')['href'] for div in soup.find_all("div",attrs={'class':'gXNuqr'})]

for num in range(len(links)):
    if links[num].find(first_part) != 0 :
       links[num] = first_part + links[num]




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path="path/to/executable")


driver.get('https://forms.gle/cHgdKMD3CL6zVkeS7')
for index in range(len(price_list)):

    driver.find_element(By.XPATH,"//input[@aria-describedby='i2 i3']").send_keys(address_list[index])

    driver.find_element(By.XPATH,"//input[@aria-describedby='i6 i7']").send_keys(price_list[index])

    driver.find_element(By.XPATH,"//input[@aria-describedby='i10 i11']").send_keys(links[index])

    driver.find_element(By.XPATH,"//div[@jsname='M2UYVd']").click()

    driver.find_element(By.LINK_TEXT,"다른 응답 제출").click()




















