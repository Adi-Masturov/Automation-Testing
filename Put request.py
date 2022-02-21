import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# Read input from Json file
file = open(r'C:\Users\adima\Documents\pythonAutomationSelenium\CreateUser.json')
json_input = file.read().split('\n')
request_json = json.dumps(json_input)

# Make PUT request with Json input body
response = requests.put(url,request_json)

# Validation response code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])