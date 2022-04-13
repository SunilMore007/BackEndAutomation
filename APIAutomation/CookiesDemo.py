import requests

url1 = "http://rahulshettyacademy.com"

cookie = {"visit-month": "February"}
response = requests.get(url1, cookies=cookie)

print(response.status_code)
# **************************************************************************
url2 = "https://httpbin.org/cookies"

cookie = {"visit-month": "February"}
response = requests.get(url2, cookies={"visit-year": "2022"})

print(response.status_code)
print(response.text)

# ********************** With Session Manager *******************************

session_variable = requests.session()
session_variable.cookies.update({"visit-month": "February"})

url2 = "https://httpbin.org/cookies"

response = session_variable.get(url2, cookies={"visit-year": "2030"})

print(response.status_code)
print(response.text)
