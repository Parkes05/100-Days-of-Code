import requests, smtplib, os
from twilio.rest import Client

class SheetManager:

    def __init__(self, token: str, endpoint: str, sheet: str):
        self.headers = {
            'Authorization': 'Bearer ' + token
        }
        self.sheet = sheet
        self.endpoint = f'{endpoint}/{self.sheet}'
    
    def get_sheet_data(self) -> list:
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()[self.sheet]
        return data
    
    def input_data(self, id, **params):
        body = {
            self.sheet: params
        }
        response = requests.put(url=f'{self.endpoint}/{id}', json=body, headers=self.headers)
        response.raise_for_status()


class FlightManager:

    def __init__(self, key: str, endpoint: str):
        self.headers = {
            'apikey': key
        }
        self.query_endpoint = f'{endpoint}/locations/query'
        self.search_endpoint = f'{endpoint}/search'
    
    def get_iata(self, **parameters) -> str:
        response = requests.get(url=self.query_endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        data = response.json()['locations'][0]['code']
        return data
    
    def get_flight_price(self, **params):
        response = requests.get(url=self.search_endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        data = response.json()['data'][0]
        return data


class NotificationManager:

    def __init__(self, account_sid: str, auth_token: str):
        self.account_sid = account_sid
        self.auth_token = auth_token

    def send_message(self, flight_data, data):
        currency = flight_data['conversion']
        country = data['city']
        iata = data['iataCode']
        client = Client(self.account_sid, self.auth_token)
        body = f'Low Price alert! Only {currency} to fly from Abuja-ABV to {country}-{iata}'

        message = client.messages \
                        .create(
                            body=body,
                            from_=os.environ['from'],
                            to=os.environ['to']
                        )

        print(message.status)

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ['email'], password=os.environ['password'])
            connection.sendmail(from_addr=os.environ['email'], to_addrs=os.environ['email'], msg=f'Subject: Cheap Flight\n\n{body}')
    

class UserInfo:

    def __init__(self):
        print('Welcome to Moxy\'s Flight Club\nWe find the best flight deals and email you.')
        self.ask_user()

    def ask_user(self):
        self.first_name = input('What is your first name?\n')
        self.last_name = input('What is your last name?\n')
        self.email = input('What is your email?\n')
        self.email_1 = input('Type your email again\n')
    
    def compare_emails(self) -> bool:
        if self.email == self.email_1:
            print('You\'re in the club!')
            return True
