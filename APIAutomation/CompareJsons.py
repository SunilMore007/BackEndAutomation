import json

# compare two jsons
with open('D:\\Python\\course.json') as r1:
    data1 = json.load(r1)  # store's as dictionary of first file

with open('D:\\Python\\course2.json') as r2:
    data2 = json.load(r2)  # store's as dictionary of first file

print(data1 == data2)
assert data1 == data2
