import requests
from Configurations import *

url = "https://api.github.com/user"

github_response = requests.get(url, verify=True, auth=(getUsername(), getPassword()))
# github_response = requests.get(url, auth=('qq', 'qq'))

print(github_response.status_code)
# ******************************* Using Session Manager ********************************************************

se = requests.session()
se.auth = auth = (getUsername(), getPassword())

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)