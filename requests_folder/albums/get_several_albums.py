import requests
from generate_token import GenerateToken


def get_several_valid_albums(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums?ids={list_of_ids}', headers=header)
    return response.json()


def get_several_invalid_albums(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums?ids={list_of_ids}', headers=header)
    return response.json()


def get_several_albums_invalid_range(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums?ids={list_of_ids}', headers=header)
    return response.json()
