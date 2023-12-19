import time

import requests
from environment import token

def check_saved_albums(list_of_ids):

    time.sleep(4)
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/me/albums/contains?ids={list_of_ids}', headers=header)
    return response
