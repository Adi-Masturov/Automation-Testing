import requests
import json
import jsonpath


url = "https://reqres.in/api/users?page=2"

# Send GET request and print response:
response = requests.get(url)
print(response)

# Display response Content
print(response.content)

# Display response headers
print(response.headers)

# Parse response to JSON format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using JSON path, print first value in the list
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

assert pages[0] == 2
