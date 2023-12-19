import requests
from generate_token import GenerateToken


def put_save_show_user(list_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.put(f'https://api.spotify.com/v1/me/shows?ids={list_ids}', headers=header)
    return response.json()
