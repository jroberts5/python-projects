import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# Constants
AMAZON_PRODUCT_LINK = "https://www.amazon.com/Celestron-NexStar-130SLT-Computerized-Telescope/dp/B0007UQNNQ"
PRICE_THRESHOLD = 800
SENDER_EMAIL = '{sender email address}'
PASSWORD = '{password for sender email}'
SMTP_SERVER = 'smtp.gmail.com'
RECIPIENT_EMAIL = "{recipient email address}"


def send_email(data):
    item_name = data['name']
    new_price = data['price']
    email_message = f"{item_name} is currently at ${new_price}! Go check it out now: {AMAZON_PRODUCT_LINK}"

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=RECIPIENT_EMAIL,
                            msg=f"Subject: New Amazon Deal! \n\n {email_message}")
        print("Email Sent")


def is_deal(current_price):
    if current_price < PRICE_THRESHOLD:
        return True
    else:
        return False


def get_item_data():
    amazon_search_headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31",
    }
    item = {}
    amazon_response = requests.get(url=AMAZON_PRODUCT_LINK, headers=amazon_search_headers)
    soup = BeautifulSoup(amazon_response.text, "lxml")
    item_price = float(soup.find(name="span", id="price_inside_buybox").get_text().replace("$", ""))
    item_name = soup.find(name="span", id="productTitle").get_text().strip()
    item['name'] = item_name
    item['price'] = item_price
    return item


# Checks the products current price - if lower than threshold, it will send an email notification of the new price
current_data = get_item_data()
if is_deal(current_data['price']):
    send_email(current_data)


