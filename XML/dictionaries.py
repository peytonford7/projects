import xmltodict

# Create dictionary
store = {
    "apples": 15,
    "bananas": 5,
    "cherries": 20
}

# Copy store and change amounts
store2 = store.copy()
store2["apples"] = 12
store2["bananas"] = 8
store2["cherries"] = 25
store2["watermelon"] = 3

# Nested dictionaries for inventory
fruit1 = {"name": "apple", "stock": 10}
fruit2 = {"name": "banana", "stock": 5}

inventory = {
    "fruit1": fruit1,
    "fruit2": fruit2
}

# Combine all dictionaries for XML
data = {
    "store": store,
    "store2": store2,
    "inventory": inventory
}

# Convert to XML and write to file
xml_string = xmltodict.unparse({"root": data}, pretty=True)

with open("output.xml", "w") as file:
    file.write(xml_string)
