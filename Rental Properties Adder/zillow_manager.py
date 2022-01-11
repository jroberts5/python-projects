import requests
from bs4 import BeautifulSoup

ZILLOW_APARTMENT_URL = "https://www.zillow.com/b/"
ZILLOW_SEARCH_URL = "{Zillo apartment/home search}"


class ZillowManager:
    def __init__(self):
        self.search_headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31",
        }

    def get_listings_data(self):
        zillow_response = requests.get(url=ZILLOW_SEARCH_URL, headers=self.search_headers)
        zillow_data = zillow_response.text
        soup = BeautifulSoup(zillow_data, "html.parser")
        listings = []

        all_links = list(dict.fromkeys([link['href'].replace('/b/', ZILLOW_APARTMENT_URL) for link in
                                        soup.find_all(name="a", class_="list-card-link")]))
        all_prices = [price.get_text().split('/')[0].split('+')[0] for price in
                      soup.find_all(name="div", class_="list-card-price")]
        all_addresses = [address.get_text() for address in soup.find_all(name="address")]
        for i in range(len(all_links)):
            new_listing = {'listing_link': all_links[i],
                           'listing_address': all_addresses[i],
                           'listing_price': all_prices[i]}
            listings.append(new_listing)
        return listings
