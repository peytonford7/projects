import json

with open('sample.json', 'r') as file:
    data = json.load(file)

print(data)