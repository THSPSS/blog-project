from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "siss9898@naver.com"
PASSWORD = "sunyoung98"



class InstaFollower:
    def __init__(self,path):
        self.driver = webdriver.Chrome(path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        self.username = self.driver.find_element(By.NAME,"username")
        self.username.send_keys(USERNAME)

        self.password = self.driver.find_element(By.NAME,"password")
        self.password.send_keys(PASSWORD)

        self.password.send_keys(Keys.ENTER)

        time.sleep(10)

        self.driver.find_element(By.CLASS_NAME,'_acan').click()

        time.sleep(10)

        self.driver.find_element(By.CLASS_NAME, '_a9_1').click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(3)

    def follow(self):
        while True:
            try:
                list_of_people = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
                for person in list_of_people:
                    if person.text == "Follow":
                        person.click()
                        time.sleep(random.randint(30, 60))
                    print(len(list_of_people))

                self.driver.execute_script("argument[0].scrollIntoView(true);", list_of_people[-1])

            except Exception as e:
                print(e)





instafollwer = InstaFollower(CHROME_DRIVER_PATH)

instafollwer.login()
instafollwer.find_followers()
instafollwer.follow()
