import requests
from generate_token import GenerateToken


def get_artists_albums(id):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/artists/{id}/albums', headers=header)
    return response.json()
