import requests
from environment import token


def del_saved_albums(list_of_ids):
    header = {'Authorization': token}
    response = requests.delete(f'https://api.spotify.com/v1/me/albums', headers=header, data=list_of_ids)
    return response.text
