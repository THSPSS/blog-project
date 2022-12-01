from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

today = datetime.date.today()
year = today.year

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# search_bar = driver.find_elements(By.NAME,"q")
# print(search_bar[0].get_attribute("placeholder"))

#logo = driver.find_element(By.CLASS_NAME,"python-logo")
#print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

#driver.find_elements(By.CSS_SELECTOR,"css_selector")

date = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')

title = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')
#
new_dict = {}
for i in range(len(date)):
    new_dict[i] = {
        "time":
            f"{year}-{date[i].text}",
        "name":
            title[i].text
    }


    # create_dict={}
    # create_dict["time"]= date_list[i]
    # create_dict["name"] = title_list[i]
    # new_dict[i] = create_dict

print(new_dict)


#driver.close()
driver.quit()#close more than one browser all browser