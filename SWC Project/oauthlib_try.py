from oauthlib.oauth2 import WebApplicationClient
import requests

client_id = 'f18aae9d971b07903c15ef36eb3e3c8a694de606'
client_secret = 'bdaa32585feffbcd48b657185ea87428fe7be467'

client = WebApplicationClient(client_id)

auth_endpoint = 'https://www.swcombine.com/ws/oauth2/auth'

url = client.prepare_request_uri(
    auth_endpoint,
    redirect_uri = 'https://localhost:80',
    scope = ['character_read'],
    state = 'sfetw45'
)

print(url)

data = client.prepare_request_body(
    code ='96dc2594ea6f108c8caa85d37693f1ec',
    redirect_uri = 'https://localhost:80',
    client_id = client_id,
    client_secret = client_secret,
    grant_type = 'authorization_code'
)

print(data)

token_url = 'https://www.swcombine.com/ws/oauth2/token'
response = requests.post(token_url, data=data)

#client.parse_request_body_response(response.text)
