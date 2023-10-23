import requests, os
import datetime as dt

NUTRITION_APP_ID = os.environ.get('nutrition_app_id')
NUTRITION_KEY = os.environ.get('nutrition_key')

nutrition_headers = {
    'x-app-id': NUTRITION_APP_ID,
    'x-app-key': NUTRITION_KEY,
}

query = input('Tell me which exercise you did: ')

nutrition_parameters = {
    'query': query,
    'gender': 'male',
    'weight_kg': 80.5,
    'height_cm': 170.2,
    'age': 28
}

nutrition_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutrition_response = requests.post(url=nutrition_exercise_endpoint, json=nutrition_parameters, headers=nutrition_headers)
nutrition_response.raise_for_status()
nutrition_data = nutrition_response.json()['exercises']

for data in nutrition_data:
    exercise = data['name'].title()
    duration = data['duration_min']
    calories = data['nf_calories']
    date = dt.datetime.now().date()
    formatted_date = date.strftime('%d-%m-%Y')
    time = dt.datetime.now().time()
    formatted_time = time.strftime('%I:%M:%S %p')

    sheety_data = {
        'sheet1': {
            'date': formatted_date,
            'time': formatted_time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories,
        }
    }
    
    sheety_headers = {
        'Authorization': 'Bearer ' + os.environ['sheety_token']
    }
    sheety_endpoint = os.environ.get('workout_url')
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_headers)
    sheety_response.raise_for_status()