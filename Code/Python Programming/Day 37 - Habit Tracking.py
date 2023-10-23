import requests, os
import datetime as dt

USER_NAME = 'parkes0'
TOKEN = os.environ.get('pixela_token')
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'
user_parameters = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'walking',
    'unit': 'meter',
    'type': 'float',
    'color': 'sora',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

current_dt = dt.datetime.now()
formatted_date = current_dt.strftime('%Y%m%d')

pixel_url_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'
pixel_values = {
    'date': formatted_date,
    'quantity': '250',
}

# response = requests.post(url=pixel_url_endpoint, json=pixel_values, headers=headers)
# print(response.text)

pixel_update_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_date}'

update_parameters = {
    'quantity': '150.5',
}

# response = requests.put(url=pixel_update_endpoint, json=update_parameters, headers=headers)
# print(response.text)

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)