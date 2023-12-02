import json
json_i=open("key.json","r")
json_road=json.load(json_i)

print(json_road["API Key"])
