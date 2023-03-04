import requests
import hashlib

# set up authentication
username = 'Demo'
password = 'Demo'
password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()

# set up the request parameters to obtain a session ID
url = 'https://suitecrmdemo.dtbc.eu/service/v4/rest.php'
params = {
    'method': 'login',
    'input_type': 'JSON',
    'response_type': 'JSON',
    'rest_data': '{"user_auth":{"user_name":"' + username + '","password":"' + password_hash + '","version":"1"},"application_name":"RestTest"}'
}

# make the request to obtain a session ID
response = requests.get(url, params=params)

# extract the session ID from the response
session_id = response.json()['id']

# use the session ID to retrieve leads data
params = {
    'method': 'get_entry_list',
    'input_type': 'JSON',
    'response_type': 'JSON',
    'rest_data': '{"session":"' + session_id + '","module_name":"Leads","query":"","order_by":"id","offset":"0","select_fields":["phone_work", "first_name", "last_name"],"max_results":"10","deleted":"0"}'
}
response = requests.get(url, params=params)
data = response.json()['entry_list']
# print(data)

def get_user_details(data):
    details = []
    for i in data:
        details.append(i['name_value_list'])
    return details

details = get_user_details(data)
# showing details of all users
for i in details:
    print(i)