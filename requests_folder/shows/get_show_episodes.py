import requests
from generate_token import GenerateToken


def get_show_episodes(id, limit, offset, market):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/shows/{id}/episodes?limit={limit}&offset={offset}&market={market}', headers=header)
    return response.json()
