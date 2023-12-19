import requests
from generate_token import GenerateToken


def get_check_saved_episodes(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/me/episodes/contains?ids={list_of_ids}', headers=header)
    return response.json()
