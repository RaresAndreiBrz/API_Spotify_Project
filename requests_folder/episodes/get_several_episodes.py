import requests
from generate_token import GenerateToken


def get_several_episodes(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/episodes?ids={list_of_ids}', headers=header)
    return response.json()


def get_several_episodes_with_market(list_of_ids, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/episodes?ids={list_of_ids}&market={market}', headers=header)
    return response.json()

