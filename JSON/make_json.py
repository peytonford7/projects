import json

# Create list of example responses
api_responses = [
    {"id": 1, "first_name": "Alice", "last_name": "Johnson"},
    {"id": 2, "first_name": "Bob", "last_name": "Smith"},
    {"id": 3, "first_name": "Charlie", "last_name": "Brown"},
    {"id": 4, "first_name": "Diana", "last_name": "Martinez"},
    {"id": 5, "first_name": "Ethan", "last_name": "Williams"}
]

# Create JSON file from responses
with open('api_responses.json', 'w') as outfile:
	for response in api_responses:
		print(json.dumps(response), file=outfile)
