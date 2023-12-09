import random
import urllib.request
import json
import hashlib

url = 'http://127.0.0.1:5000/api/v1/get_user_info'

app_id = 'MZFiLAzmJu'
app_key = 'vUCiKf167oNUfpdbsxKs'
session = 'wSYReKptTY5P8ZT9Vlpy'
username = 'test3'
salt = str(random.randint(1, 100000))
sign_str = app_id + app_key + session + username + salt
sign = hashlib.sha256(sign_str.encode()).hexdigest()

data = {
    'app_id': app_id,
    'session': session,
    'username': username,
    'salt': salt,
    'sign': sign
}
print(data)
headers = {'Content-Type': 'application/json'}
json_data = json.dumps(data).encode('utf8')

req = urllib.request.Request(url=url, data=json_data, headers=headers)
response = urllib.request.urlopen(req)
result = response.read().decode('utf8')
print(result)
