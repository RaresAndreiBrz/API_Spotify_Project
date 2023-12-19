import requests
from generate_token import GenerateToken


def get_episode(id, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/episodes/{id}?market={market}', headers=header)
    return response.json()

