import requests
from generate_token import GenerateToken


def put_save_albums(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.put(f'https://api.spotify.com/v1/me/albums', headers=header, data=list_of_ids)
    return response.json()
