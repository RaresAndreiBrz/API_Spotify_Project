import requests
from generate_token import GenerateToken


def del_saved_show_user(list_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.delete(f'https://api.spotify.com/v1/me/shows?ids={list_ids}', headers=header)
    return response.json()
