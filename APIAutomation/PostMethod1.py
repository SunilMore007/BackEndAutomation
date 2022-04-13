import time

import requests
from payload import *
from Configurations import *
import configparser

addbook_response = requests.post(getConfig()["API"]["endpoint"] + '/Library/Addbook.php',
                                 json=addBookPayload("hyrtet554", "4344rd434"),
                                 headers={'Content-type': 'application/json'}, )

print(addbook_response.json())
json_response = addbook_response.json()

bookID = json_response['ID']  # got the Book ID from response
print(bookID)

# ************ Delete the book by Retrieving ID from Previous request
time.sleep(5)

Delete_book_response = requests.post('http://216.10.245.166/Library/DeleteBook.php',
                                     json={"ID": bookID}, headers={'Content-Type': 'application/json'}, )
print(Delete_book_response.status_code)
json_resp = Delete_book_response.json()
print(json_resp)
print(json_resp['msg'])



