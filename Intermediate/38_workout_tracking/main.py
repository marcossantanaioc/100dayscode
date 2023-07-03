import requests
from typing import Dict
import datetime as dt
import os

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('NutriAPPKey')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
SHEETY_URL = 'https://api.sheety.co/a308f80c67a624a417930e2f946f5632/myWorkouts/workouts'
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'


class FitnessTracker:

    def __init__(self, query: str, params: Dict = None):
        self.query = query
        self.params = params
        self.params['query'] = query

    @property
    def header(self):
        return {'x-app-id': APP_ID, 'x-app-key': API_KEY, 'x-remote-user-id': '0'}

    @property
    def sheety_header(self):
        return {"Authorization": "Bearer markinsldp33"}

    @property
    def time(self):
        now = dt.datetime.now()
        return now.time().strftime('%H:%M:%S')

    @property
    def date(self):
        now = dt.datetime.now()
        return now.date().strftime('%d/%m/%Y')

    @property
    def data(self):
        response = requests.post(url=URL, json=params, headers=self.header)
        response.raise_for_status()
        data_raw = response.json()['exercises']

        data_to_publish = []

        for exercise in data_raw:
            data = {'workout': {}}
            exercise['exercise'] = exercise.pop('name').title()
            exercise['duration'] = exercise.pop('duration_min')
            exercise['calories'] = exercise.pop('nf_calories')
            exercise['date'] = self.date
            exercise['time'] = self.time
            exercise.pop('tag_id')
            exercise.pop('user_input')
            exercise.pop('photo')
            exercise.pop('met')
            exercise.pop('compendium_code')
            exercise.pop('benefits')
            exercise.pop('description')
            data['workout'] = exercise
            data_to_publish.append(data)
        return data_to_publish

    def publish_data(self):
        for ex in self.data:
            response = requests.post(SHEETY_URL, json=ex, headers=self.sheety_header)
            response.raise_for_status()
        return self.data


if __name__ == '__main__':
    user_input = str(input("Tell me which exercises you did: "))
    params = {'gender': 'male', 'weight_kg': 90, 'height_cm': 183, 'age': 33}
    tracker = FitnessTracker(query=user_input, params=params)
    data = tracker.publish_data()
    print(data)
