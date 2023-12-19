import requests
from generate_token import GenerateToken


def put_save_episode(list_of_ids):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    data1 = {"ids":[list_of_ids]}
    response = requests.put(f'https://api.spotify.com/v1/me/episodes', headers=header, data=data1)
    return response.json()

