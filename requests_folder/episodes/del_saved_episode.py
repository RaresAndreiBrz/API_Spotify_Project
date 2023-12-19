import requests

from environment import token


def del_saved_episode(list_of_ids):
    header = {'Authorization': token}
    data1 = {"ids": [list_of_ids]}
    response = requests.delete(f'https://api.spotify.com/v1/me/episodes', headers=header, data=data1)
    return response.json()
