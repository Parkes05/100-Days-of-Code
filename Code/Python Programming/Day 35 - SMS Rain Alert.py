import requests, smtplib, os

api_key = os.environ.get('weather_api_key')
weather_url = 'http://api.weatherapi.com/v1/forecast.json'
parameters = {
    'q': 'Abuja',
    'key': api_key,
    'days': 1,
}

response = requests.get(url=weather_url, params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()
hour_list = data['forecast']['forecastday'][0]['hour']
sliced_hour_list = hour_list[:12]

will_rain = False

for element in sliced_hour_list:
    if element['will_it_rain'] == 1:
        will_rain = True

if will_rain:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ.get('email'), password=os.environ.get('passwrd'))
        connection.sendmail(from_addr=os.environ.get('email'), to_addrs=os.environ.get('email'), 
                        msg='Subject:Rain Condition\n\nIt will rain today. Bring an umbrella')