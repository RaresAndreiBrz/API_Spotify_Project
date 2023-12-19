import requests
from generate_token import GenerateToken


def get_single_category(category_id, locale, country):
    token_returned = GenerateToken.authorization()
    header = {'Authorization': token_returned}
    response = requests.get(f'https://api.spotify.com/v1/browse/categories/?category_id={category_id}&locale={locale}&country={country}', headers=header)
    return response.json()

