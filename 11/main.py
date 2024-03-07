import json
# Parsing a json string 
user = ' {"username": "John deo" , "age" : 34} '

docs = json.loads(user)
# print(docs["username"])

# Stringifying  json
user = {"username": "John deo" , "age" : 34}

stringified_docs = json.dumps(user)
print(stringified_docs["username"])