import os
import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

# Constants
CHROME_DRIVER_PATH = "C:\Development\Development\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = "nasa"
INSTAGRAM_USERNAME = os.environ['INSTAGRAM_USERNAME']
INSTAGRAM_PW = os.environ['INSTAGRAM_PW']
INSTAGRAM_LOGIN_URL = "https://www.instagram.com/accounts/login"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get(INSTAGRAM_LOGIN_URL)
        time.sleep(2)
        instagram_email = self.driver.find_element_by_name("username")
        instagram_email.send_keys(INSTAGRAM_USERNAME)
        instagram_pw = self.driver.find_element_by_name("password")
        instagram_pw.send_keys(INSTAGRAM_PW)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

    def find_followers(self):
        time.sleep(3)
        search_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_field.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)
        search_result = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        search_result.click()
        time.sleep(3)
        follower_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_link.click()
        time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector(".PZuss button")
        for follow in follow_buttons:
            try:
                follow.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


# Creates the insta bot - navigates to an insta account - adds followers
instagram_bot = InstaFollower(driver_path=CHROME_DRIVER_PATH)
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()
instagram_bot.driver.close()
