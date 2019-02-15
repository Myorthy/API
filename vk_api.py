from urllib.parse import urlencode
APP_ID = 0000000
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status, friends',
    'response_type': 'token',
    'v': '5.92',
}
TOKEN = 'acce4e3112156fc596406ce'
params = {
'v': '5.92'
}
response = requests.get('https://api.vk.com/method/status.get', params)



print('?'.join((AUTH_URL, urlencode(auth_data))))
