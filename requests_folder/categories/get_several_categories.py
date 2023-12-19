import requests
from generate_token import GenerateToken


def get_several_categories(locale, limit, offset, country):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/browse/categories?locale={locale}&limit={limit}&offset={offset}&country={country}', headers=header)
    return response.json()



