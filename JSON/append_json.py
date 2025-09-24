import json

# Create a list to append to our JSON file
new_data = {"id": 4, "first_name": "Peyton", "last_name": "Ford"}

# Open JSON file in read mode
with open('sample.json', 'r') as file:
	data = json.load(file)

# Append the new data	
data.append(new_data)

# Write the updated data back to the JSON file
with open('sample.json', 'w') as file:
	json.dump(data, file, indent=4)
