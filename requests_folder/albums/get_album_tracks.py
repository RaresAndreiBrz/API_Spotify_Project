import requests
from generate_token import GenerateToken


def get_albums_tracks(id):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}/tracks', headers=header)
    return response.json()


def get_albums_tracks_withParams_Limit(id, limit):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}/tracks?limit={limit}', headers=header)
    return response.json()


def get_albums_tracks_withParams_Limit_Offset(id, limit, offset):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}/tracks?offset={offset}&limit={limit}', headers=header)
    return response.json()


def get_albums_tracks_withParams_Limit_Offset_Market(id, market, limit, offset):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}/tracks?market{market}&offset={offset}&limit={limit}', headers=header)
    return response.json()
