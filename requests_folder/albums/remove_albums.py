import requests
from generate_token import GenerateToken


def remove_albums(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.delete(f'https://api.spotify.com/v1/me/albums?ids={list_of_ids}', headers=header)
    return response.json()
