import requests
from payload import *

url = 'http://216.10.245.166/Library/Addbook.php'
addbook_response = requests.post(url,
                                 json=addBookPayload("djsahdjsk7687", "dsadasd9a899"), headers={'Content-type': 'application/json'}, )

print(addbook_response.json())
json_response = addbook_response.json()
print(type(json_response))

bookID = json_response['ID']  # got the Book ID from response

# ************ Delete the book by Retrieving ID from Previous request

Delete_book_response = requests.post('http://216.10.245.166/Library/DeleteBook.php',
                                     json={"ID": bookID}, headers={'Content-Type': 'application/json'}, )
print(Delete_book_response.status_code)
json_resp=Delete_book_response.json()
print(json_resp)
print(json_resp['msg'])
