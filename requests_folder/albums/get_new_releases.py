import requests
from generate_token import GenerateToken


def get_new_releases():
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/browse/new-releases', headers=header)
    return response.json()
