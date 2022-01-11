import time
from selenium import webdriver

GOOGLE_FORM_SUBMISSION_URL = "{Google Form Link}"

class GoogleManager:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def submit_google_form(self, zillow_data):
        self.driver.get(GOOGLE_FORM_SUBMISSION_URL)
        time.sleep(2)

        for listing in zillow_data:
            address_field = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_field.send_keys(listing['listing_address'])
            time.sleep(1)

            price_field = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field.send_keys(listing['listing_price'])
            time.sleep(1)

            link_field = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field.send_keys(listing['listing_link'])
            time.sleep(1)

            submit_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
            submit_button.click()
            time.sleep(3)

            new_submission = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            new_submission.click()
