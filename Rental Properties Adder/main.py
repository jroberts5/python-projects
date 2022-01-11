from bs4 import BeautifulSoup
from google_manager import GoogleManager
from zillow_manager import ZillowManager

'''
Overview: Gets rent listing for city/location - automatically submits all scraped listing to a 
google form
'''

CHROME_DRIVER_PATH = "C:\Development\Development\chromedriver_win32\chromedriver.exe"

# Gets listing data from Zillow
zillow_manager = ZillowManager()
listing_data = zillow_manager.get_listings_data()

# Sends the data to the Google Form
google_manager = GoogleManager(driver_path=CHROME_DRIVER_PATH)
google_manager.submit_google_form(listing_data)

