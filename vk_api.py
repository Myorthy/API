import requests
from urllib.parse import urlencode

APP_ID = 6862932
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status, friends',
    'response_type': 'token',
    'v': '5.92',
}
TOKEN = 'acce4e3112156fc596406cec7c3c201ce0d4da214bc5ea6a82eb0e2ab9cdc1a3e4059ef1d97441dc71b88'

# print('?'.join((AUTH_URL, urlencode(auth_data))))

class User:

    def __init__(self, token):
        self.token = token

    def get_params(self):
        return {
        'v': '5.92',
        'access_token': TOKEN,
        }

    def get_status(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/status.get', params)
        return response.json()

    def set_status(self, text):
        params = self.get_params()
        params['text'] = text
        response = requests.get('https://api.vk.com/method/status.set', params)
        return response.json()

    def mutual_friends(self, user_id):
        params = self.get_params()
        params['target_uid'] = user_id
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.json()





user = User(TOKEN)
print(user.get_status())
print(user.mutual_friends(90826116))
