import requests

#response = requests.get("http://rahulshettyacademy.com", allow_redirects=False)
response = requests.get('https://www.google.com/')
print(response.history)
print(response.status_code)

