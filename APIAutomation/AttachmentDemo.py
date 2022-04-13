import requests

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
# 9843217
file = {"file": open('D:\\katrina.jpg', 'rb')}

response = requests.post(url, files=file)
print(response.status_code)      #200

print(response.text)  #{"code":200,"type":"unknown","message":"additionalMetadata: null\nFile uploaded to ./katrina.jpg, 35060 bytes"}
