import requests
import pandas as pd
from datetime import datetime
import time
from spotify_vars import KEY, SECRET


class SpotifyAPI:
    def __init__(self, user_key: str, secret: str):
        self.user_key = user_key
        self.secret = secret

    @property
    def url(self):
        return 'https://accounts.spotify.com/api/token'

    @property
    def grant_type(self):
        return 'client_credentials'

    @property
    def authentication(self):
        return {'client_id': self.user_key, 'grant_type': self.grant_type, 'client_secret': self.secret}

    @property
    def token(self):
        response = requests.post(self.url, data=self.authentication, json=True)
        response.raise_for_status()
        print(response.status_code)
        return response.json()['access_token']

    @property
    def headers(self):
        return {'Authorization': 'Bearer {token}'.format(token=self.token)}

    def query_by_artist(self, artist_id: str):
        URL = 'https://api.spotify.com/v1/artists'
        params = {'ids': artist_id}

        # actual GET request with proper header
        response = requests.get(URL, params=params, headers=self.headers)
        return response.json()['artists']


if __name__ == '__main__':
    spotify = SpotifyAPI(user_key=KEY, secret=SECRET)
    ACCESS_TOKEN = spotify.token
