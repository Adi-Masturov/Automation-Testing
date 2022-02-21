import requests
import json
import jsonpath

payload = {'Username': 'Adi', 'Password': 'testing'}

# Make POST request with Json input body
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()

print(r_dict['form'])

# Post request from Json file
url = "https://reqres.in/api/users"

# Read input from Json file
file = open(r'C:\Users\adima\Documents\pythonAutomationSelenium\CreateUser.json')
json_input = file.read().split('\n')
request_json = json.dumps(json_input)

# Make POST request with Json input body
response = requests.post(url,request_json)

# Validation response code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get('Content-Length'))

# Parse response to Json format
response_json = json.loads(response.text)

# Pick ID using Json Path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])
