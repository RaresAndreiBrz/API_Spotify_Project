import requests
from generate_token import GenerateToken


def get_artist_related_artists(id):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/artists/{id}/related-artists', headers=header)
    return response.json()
