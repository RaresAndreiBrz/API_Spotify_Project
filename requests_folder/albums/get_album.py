import requests
from generate_token import GenerateToken


def get_album_without_market(id):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}', headers=header)
    return response


def get_album_with_valid_market(id, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}?market={market}', headers=header)
    return response


def get_album_with_invalid_market(id, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}?market={market}', headers=header)
    return response
