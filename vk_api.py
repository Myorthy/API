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
class User_id:
    def __init__(self, id):
        self.id = id


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
        response_1 = requests.get('https://api.vk.com/method/friends.getMutual', params)
        friends = response_1.json()['response']
        friend_list = []
        for friend in friends:
            friend_list.append(User_id(friend))
        return friend_list


# user = User(TOKEN)
# print(user.get_status())
print(user.mutual_friends(90826116))
# print(user)

# user = User_id(90826116)
# user = f'https://vk.com/id{user.id}'
# print(user)
