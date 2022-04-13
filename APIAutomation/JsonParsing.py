import json

courses = '{"name" : "SunilMore" , "languages": ["java", "python"]}'

# load is the method parse the jsonstring and retrurns dictionary

dec_courses = json.loads(courses)
print(type(dec_courses))
print(dec_courses)

print(dec_courses['name'])

# list_langauges=dec_courses['languages']
# print(type(list_langauges))
# print(list_langauges)
# print(list_langauges[0])

# IN Single Statement
print(dec_courses['languages'][0])

# ******************* parse content present in json file *********************
#
# with open('D:\\Python\\course.json') as f:
#     data = json.load(f)
#     print(data)
#     print(type(data))
#     #   print(data['widget'])
#     print(data['widget']['image']['src'])
#     print(data['widget']['image'][2])


with open('D:\\Python\\course2.json') as f1:
    data = json.load(f1)
    print(data['course'])
    print(type(data['course']))
    for c in data['course']:
        print(c)
        if c['title'] == "Cypress":
            print(c['price'])
            assert c['price'] == 30


