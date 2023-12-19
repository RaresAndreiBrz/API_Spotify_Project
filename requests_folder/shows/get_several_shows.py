import requests
from generate_token import GenerateToken


def get_several_shows(list_of_ids, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/shows?ids={list_of_ids}&market={market}', headers=header)
    return response.json()
