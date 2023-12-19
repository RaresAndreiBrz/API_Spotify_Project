import requests
from generate_token import GenerateToken


def get_users_saved_episodes(limit, offset, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/me/episodes?limit={limit}&offset={offset}&market={market}', headers=header)
    return response.json()

