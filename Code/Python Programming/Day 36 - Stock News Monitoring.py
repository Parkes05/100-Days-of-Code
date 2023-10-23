import os, requests
# import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_url = 'https://www.alphavantage.co/query'
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.environ.get('alphavantage_api_key')
}

response = requests.get(url=stock_url, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
daily = stock_data['Time Series (Daily)']

# current_dt = dt.datetime.now()
# number = 1
# increase_number = True
# while increase_number:
#     try:
#         previous_dt = current_dt - dt.timedelta(days=number)
#         previous_stock = daily[str(previous_dt.date())]
#     except KeyError:
#         number += 1
#     else:
#         increase_number = False
stock_data_list = [value for (key, value) in daily.items()]
# stock_dates = [key for (key, value) in daily.items()]
yesterday_stock_close = float(stock_data_list[0]['4. close'])
daybefore_stock_close = float(stock_data_list[1]['4. close'])
percentage_diff = ((yesterday_stock_close - daybefore_stock_close) / yesterday_stock_close) * 100

image = None
if percentage_diff > 0:
    image = '🔺'
else:
    image = '🔻'

if abs(percentage_diff) > 5:
    news_url = 'https://newsapi.org/v2/everything'
    news_parameters = {
        'apiKey': os.environ.get('news_api_key'),
        'qInTitle': COMPANY_NAME,
        # 'from': stock_dates[0],
        # 't0': stock_dates[1],
        # 'language': 'en',
        # 'sortBy': 'relevancy'
    }

    response_1 = requests.get(url=news_url, params=news_parameters)
    response_1.raise_for_status()
    news_data = response_1.json()
    news_articles = news_data['articles'][:3]

    formatted_text = [f"{STOCK}: {image}{round(abs(percentage_diff))}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in news_articles]
    
    account_sid = os.environ.get('twilio_sid')
    auth_token = os.environ.get('twilio_token')
    client = Client(account_sid, auth_token)

    for text in formatted_text:
        message = client.messages \
                        .create(
                            from_='+17203100864',
                            to=os.environ.get('number'),
                            body=text)

        print(message.status)