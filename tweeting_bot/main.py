from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = "sunyeongbang98@gmail.com"


class InternetSpeedTwitterBot:
    def __init__(self,path):
        self.driver = webdriver.Chrome(path)
        self.up = 0
        self.down = 0


    def get_internet_speed(self,up,down):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME,"js-start-test").click()
        time.sleep(67)
        self.down_speed = self.driver.find_element(By.CLASS_NAME,"download-speed").text
        self.up_speed = self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        print(f"up:{self.up_speed}\n down:{self.down_speed} ")
        if float(self.down_speed) <= down or float(self.up_speed) <= up:
            self.tweet_at_provider(self, self.down_speed, self.up_speed, TWITTER_EMAIL)



    def tweet_at_provider(self,down,up,email):
        self.driver.get("https://twitter.com/")
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/div[3]/div[1]').click()


twitterbot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

twitterbot.get_internet_speed(PROMISED_UP,PROMISED_DOWN)


# driver = webdriver.Chrome(CHROME_DRIVER_PATH)
# driver.get("https://twitter.com/")
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a').click()
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]').click()
# email = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
# email.send_keys(TWITTER_EMAIL)
# email.send_keys(Keys.ENTER)
# time.sleep(3)
# keys = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[1]')
# keys.send_keys("")
# keys.send_keys(Keys.ENTER)


#-------------------------------------
#
# def tweet_at_provider(self):
#     self.driver.get("https://twitter.com/login")
#
#     time.sleep(2)
#     email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
#     password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
#
#     email.send_keys(TWITTER_EMAIL)
#     password.send_keys(TWITTER_PASSWORD)
#     time.sleep(2)
#     password.send_keys(Keys.ENTER)
#
#     time.sleep(5)
#     tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
#
#     tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
#     tweet_compose.send_keys(tweet)
#     time.sleep(3)
#
#     tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
#     tweet_button.click()
#
#     time.sleep(2)
#     self.driver.quit()