import requests

auth_endpoint = "https://www.swcombine.com/ws/oauth2/auth/"
client_id = "client_id=f18aae9d971b07903c15ef36eb3e3c8a694de606"
client_secret = "client_secret=bdaa32585feffbcd48b657185ea87428fe7be467"
type = "response_type=code"
redirect = "redirect_uri=https://localhost:80"
scope = "scope=character_read"
grant_type = "grant_type=authorization_code"
#state = "state=profile&"
auth_url = auth_endpoint+"?"+client_id+"&"+type+"&"+redirect+"&"+scope

code = "code=eaf0becee6c6d668bae3f1edc2f6c758"

token_endpoint = "https://www.swcombine.com/ws/oauth2/token/"
token_url = token_endpoint+"?"+grant_type+"&"+code+"&"+redirect+"&"+client_id+"&"+client_secret
print(token_url)



#print(combined_url)

#response = requests.post(token_url).json
#print(response)
