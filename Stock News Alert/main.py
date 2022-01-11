'''
Overview: Checks last two days of closing prices for stock. If prices change more than 5%, an sms
is sent with an alert of the price change with a news article regarding that company.
'''

import os
import requests
from twilio.rest import Client

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = 'Telsa Inc.'
TWILIO_NUMBER = '[Twilio Phone Number]'
PHONE_NUMBER = '[Some phone number]'
INCREASE_ARROW = '🔺'
DECREASE_ARROW = '🔻'

# News API
NEWS_API_KEY = os.environ['NEWS_API']
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q={STOCK_NAME}&apiKey={NEWS_API_KEY}"

# Stock(Alphavantage) API
ALPHAVANTAGE_API_KEY = os.environ['ALPHAVANTAGE_API_KEY']
STOCK_ENDPOINT = f"https://www.alphavantage.co/query?"

stock_api_params = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY,

}


# SMS(Twilio) API
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']


def send_sms(news, change, percentage):
    # Info: Uses data from 'compare_closing_costs' to send SMS message.
    direction = ''
    if change == 'Negative':
        direction = DECREASE_ARROW
    if change == 'Positive':
        direction = INCREASE_ARROW
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body=f"Company:{COMPANY_NAME} | {direction}{round(percentage, 3)}%\nHeadline:{news['title']}\n{news['description']}",
        from_=f"{TWILIO_NUMBER}",
        to=f"{PHONE_NUMBER}"
    )
    print(message.status)


def get_news():
    # Info: Extracts an article from the News API with that company's stock name
    news_response = requests.get(url=NEWS_ENDPOINT)
    news_data = news_response.json()
    news_story = news_data['articles'][:1]
    news_response.raise_for_status()
    return {'title': news_story[0]['title'], 'description': news_story[0]['description']}


def compare_closing_prices():
    # Info: Compares the last two closing prices of the days - if more then 5% sends sms
    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_api_params)
    stock_data = stock_response.json()
    two_stock_days = [{days: values['4. close']} for (days, values) in stock_data['Time Series (Daily)'].items()][:2]
    closing_date_yesterday = "".join([date for date in two_stock_days[0]])
    closing_price_yesterday = float(two_stock_days[0][closing_date_yesterday])
    closing_date_two_days_ago = "".join([date for date in two_stock_days[1]])
    closing_price_two_days_ago = float(two_stock_days[1][closing_date_two_days_ago])
    price_difference = closing_price_yesterday - closing_price_two_days_ago

    if price_difference < 0:
        positive_or_negative = 'Negative'
    else:
        positive_or_negative = 'Positive'

    percentage_change = abs((price_difference / closing_price_two_days_ago) * 100)
    if percentage_change > 5:
        send_sms(news=get_news(), change=positive_or_negative, percentage=percentage_change)

# START HERE
compare_closing_prices()
