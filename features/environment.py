import requests

#  This method will execute after feature is executed
from Utilities.resources import APIResources


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php',
                                            json={"ID": context.bookID}, headers={'Content-Type': 'application/json'}, )
        print(response_deleteBook.status_code)
        json_resp = response_deleteBook.json()
        print(json_resp)
        print(json_resp['msg'])
