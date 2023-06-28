import requests
import url_addys as ua
from oauthlib.oauth2 import WebApplicationClient

client_id = 'f18aae9d971b07903c15ef36eb3e3c8a694de606'
client_secret = 'bdaa32585feffbcd48b657185ea87428fe7be467'
client = WebApplicationClient(client_id)
redirect_uri='http://localhost:8000'

authrequrl = client.prepare_request_uri(
    ua.authme,
    redirect_uri='http://localhost:8000',
    scope = ['character_read']
)
print(authrequrl)

ret_token = '9311023781e95db8a8450404cf943a98'


# authsendurl = client.create_code_verifier(
#     ua.authToken,
#     code=ret_token,
#     client_secret=client_secret,
#     redirect_url='http://localhost:1099'
# )
url = ua.authToken+"?code="+ret_token+"&client_id="+client_id+"&client_secret="+client_secret+"&redirect_uri="+redirect_uri+"&grant_type=authorization_code"
# response = requests.post(ua.authToken?client_id)

