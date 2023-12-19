import requests
from generate_token import GenerateToken


def get_artist_top_track(id, country):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/artists/{id}/top-tracks?country={country}', headers=header)
    return response.json()
