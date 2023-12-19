import requests
from generate_token import GenerateToken


def get_saved_albums(limit, offset):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/me/albums?limit={limit}&offset={offset}', headers=header)
    return response.json()


def get_saved_albums_with_market(limit, offset, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/me/albums?limit={limit}&offset={offset}&market={market}', headers=header)
    return response.json()
