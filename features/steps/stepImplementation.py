import requests
from behave import *

from APIAutomation import payload
from APIAutomation.Configurations import getConfig, getUsername, getPassword
from APIAutomation.payload import *
import requests
import configparser

from Utilities.resources import APIResources


@given('The Book details which needs to be added to library')
def step_implementation(context):
    context.url = getConfig()["API"]["endpoint"] + '/Library/Addbook.php'
    context.header = {'Content-type': 'application/json'}
    context.payload1 = addBookPayload("543rewrrw", "545dfdde")


@when('We execute the ADDBook PostAPI Method')
def step_impl(context):
    context.addbook_response = requests.post(context.url, json=context.payload1, headers=context.header, )


@then('Book is successfully Added')
def step_impl(context):
    print(context.addbook_response.json())
    json_response = context.addbook_response.json()
    print(type(json_response))

    context.bookID = json_response['ID']  # got the Book ID from response
    print(context.bookID)
    assert json_response['Msg'] == 'successfully added'


@given('The Book details with {isbn} and {aisle}')
def step_implementation(context, isbn, aisle):
    context.url = getConfig()["API"]["endpoint"] + '/Library/Addbook.php'
    context.header = {'Content-type': 'application/json'}
    context.payload1 = addBookPayload(isbn, aisle)


@given('i have github auth credentials')
def step_implementation(context):
    context.se = requests.session()
    context.se.auth = auth = (getUsername(), getPassword())


@when(u'i have getRepo API of github')
def step_impl(context):
    context.response = context.se.get(APIResources.GithubUrl)


@then(u'Status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
