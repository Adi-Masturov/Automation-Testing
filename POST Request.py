import requests

payload = {'Username': 'Adi', 'Password': 'testing'}

# Make POST request with Json input body
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()

print(r_dict['form'])


