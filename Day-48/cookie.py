import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

big_timeout = time.time() + 60*6
check = time.time()+5

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie")

cookie = driver.find_element(By.ID,"cookie")

right_panel = driver.find_elements(By.CSS_SELECTOR,"#store div")
right_panel_ids = [value.get_attribute("id") for value in right_panel]


# right_panel_money = [value.text for value in right_panel]
# right_panel_money.pop()
#
# right_panel_name = [value.split("-")[0].strip() for value in right_panel_money]
# print(right_panel_name)
#
# right_panel_money = [value.split("-")[1].strip() for value in right_panel_money]
# print(right_panel_money)

#
while True:
    cookie.click()

    #every 5 seconds:
    if time.time() > check:

            all_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
            item_price = []


            for price in all_price:
                price_text = price.text
                if price_text != "":
                    cost = int(price_text.split("-")[1].strip().replace(",",""))
                    item_price.append(cost)



            #create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_price)):
                cookie_upgrades[item_price[n]] = right_panel_ids[n]

            #get current cookie money:
            money = driver.find_element(By.ID, "money").text
            if "," in money:
                money = money.replace(",","")
            cookie_count = int(money)

            #find upgrades that we can currently afford
            affordable_upgrades = {}
            for price, id in cookie_upgrades.items():
                if cookie_count > price:
                    affordable_upgrades[price] = id

            highest_price = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price]
            driver.find_element(By.ID,to_purchase_id).click()

            check = time.time() + 5


    if time.time() > big_timeout:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)
        break
#
#
#
















# while time.time() < timeout:
#     print(time.time())
#
# print("timeout")

