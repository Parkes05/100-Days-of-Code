import os
from flighty_class_39_40 import *
import datetime as dt
from pprint import pprint

user_id = 0

sheet_token = os.environ['flight_sheety_token']
sheet_endpoint = os.environ['sheet_endpoint']

flight_endpoint = 'https://api.tequila.kiwi.com'
flight_key = os.environ['flight_key']

account_sid = os.environ['twilio_sid']
auth_token = os.environ['twilio_token']

sheet_manager = SheetManager(sheet_token, sheet_endpoint, 'sheet1')
user_sheet = SheetManager(sheet_token, sheet_endpoint, 'users')
flight_manager = FlightManager(flight_key, flight_endpoint)
notification_manager = NotificationManager(account_sid, auth_token)
user_info = UserInfo()
details = user_info.compare_emails()

if details:
    user_id += 1
    user_sheet.input_data(user_id, firstName=user_info.first_name, lastName=user_info.last_name, email=user_info.email)


sheet_data = sheet_manager.get_sheet_data()
# pprint(sheet_data)

for data in sheet_data:
    if data['iataCode'] == '':
        location = data['city']
        iata_data = flight_manager.get_iata(term=location, location_types='city')
        sheet_manager.input_data(data['id'], iataCode=iata_data)

for data in sheet_data:
    if data['lowestPrice'] == '':
        flight_data = flight_manager.get_flight_price(fly_from='ABV', fly_to=data['iataCode'], date_from='30/09/2023', date_to='30/12/2023')
        pprint(flight_data)
        sheet_manager.input_data(data['id'], lowestPrice=flight_data['fare']['adults'])

from_ = dt.datetime.now() + dt.timedelta(days=1)
f_from = from_.strftime('%d/%m/%Y')
to_ = dt.datetime.now() + dt.timedelta(days=181)
f_to = to_.strftime('%d/%m/%Y')

for data in sheet_data:
    flight_data = flight_manager.get_flight_price(fly_from='ABV', fly_to=data['iataCode'], date_from=f_from, date_to=f_to)
    lowest_price = flight_data['fare']['adults']
    if lowest_price < data['lowestPrice']:
        notification_manager.send_message(data=data, flight_data=flight_data)