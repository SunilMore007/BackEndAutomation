import json

import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty2'}, )

print(response.text)
print(type(response.text))
response_dict = json.loads(response.text)
print(response_dict[0])
print(response_dict[0]['book_name'])