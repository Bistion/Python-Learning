# Address for OAuth
authme = "https://www.swcombine.com/ws/oauth2/auth/"

# Auth Token to run after authme
authToken = "https://www.swcombine.com/ws/oauth2/token/"

# performs a helloauth call to see if client has access to the resource
# 200 response means OK
# 404 response means unauthorizedY
helloauth = "https://www.swcombine.com/ws/v2.0/api/helloauth[/]"

# Use this api call to list privs you currently have access to
listprivs = "https://www.swcombine.com/ws/v2.0/api/permissions[/]"

# This URL works to request a token by its self.
url = "https://www.swcombine.com/ws/oauth2/auth/?client_id=f18aae9d971b07903c15ef36eb3e3c8a694de606&response_type=code&redirect_uri=https://localhost:80&scope=character_read&"