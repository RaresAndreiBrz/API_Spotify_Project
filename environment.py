from generate_token import GenerateToken

token_object = GenerateToken()
token = token_object.authorization()
token_object.close()
