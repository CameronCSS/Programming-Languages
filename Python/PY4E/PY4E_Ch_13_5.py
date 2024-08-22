import json

data = '''{
"name" : "Chuck",
"phone" : {
"type" : "intl",
"number" : "+1 734 303 4456"
},
"email" : {
"hide" : "yes"
}
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])


input = '''[
{"id" : "001",
"x" : "2",
"name" : "Chuck"
},
{"id" : "009",
"x" : "7",
"name" : "Chuck"
}
]
'''

new_info = json.loads(input)
print('User count:', len(new_info))
for item in new_info:
    print('name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])