import json

import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty2'}, )

# print(response.text)
# print(type(response.text))
# response_dict = json.loads(response.text)
# print(response_dict[0]['book_name'])

# ******************to convert the response in json list format**************************
Josn_response = response.json()
print(Josn_response)
print(type(Josn_response))
print("book Name is " + Josn_response[0]['book_name'])
print(response.status_code)  # to check status code
assert response.status_code == 200
print(response.headers)  # to print headers
# print(type(response.headers))

# print(response.headers['Content-Type'])
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'  # validate the content type
print(response.cookies)  # to print the cookies

# **************************Retrieve the book details with ISBN= bnid34 **********************************************
for actual_book in Josn_response:
    # print(type(actual_book))
    if actual_book['isbn'] == 'bcz88effed':
        print(actual_book)
        break

expected_book = {'book_name': 'learn Appium Automation with Java', 'isbn': 'bcz88effed', 'aisle': '20027'}

assert actual_book == expected_book
