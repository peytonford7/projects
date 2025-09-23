# Dictionaries
store = {
    "apples": 10,
    "bananas": 5
}

store2 = dict(oranges=12, grapes=8)

print(store)
print(store2)
print(type(store))
print(len(store))

# Access items
print(store["apples"])
print(store.get("bananas"))

# Keys, values, items
print(store.keys())
print(store.values())
print(store.items())

# Check if a key exists
print("apples" in store)
print("mango" in store)

# Change values
store["apples"] = 15
store.update({"pears": 7})
print(store)

# Remove items
print(store.pop("pears"))
print(store)

store["cherries"] = 20
print(store)

print(store.popitem())
print(store)

# Delete and clear
store["kiwi"] = 9
del store["kiwi"]
print(store)

store2.clear()
print(store2)

# Copying dictionaries
store2 = store.copy()
store2["watermelon"] = 3
print("Original:", store)
print("Copy:", store2)

# Nested dictionaries
fruit1 = {"name": "apple", "stock": 10}
fruit2 = {"name": "banana", "stock": 5}

inventory = {
    "fruit1": fruit1,
    "fruit2": fruit2
}

print(inventory)
print(inventory["fruit1"]["name"])

# Sets
basket = {"apple", "banana", "orange"}
basket2 = set(("apple", "banana", "orange"))

print(basket)
print(basket2)
print(type(basket))
print(len(basket))

# Duplicates not allowed
basket = {"apple", "apple", "banana"}
print(basket)

# Check membership
print("banana" in basket)

# Add items
basket.add("pear")
print(basket)

# Merge sets
basket.update({"kiwi", "grape"})
print(basket)

# Union
a = {"apple", "banana"}
b = {"cherry", "banana"}
print(a.union(b))

# Intersection
a.intersection_update(b)
print(a)

# Symmetric difference
a = {"apple", "banana"}
b = {"banana", "cherry"}
a.symmetric_difference_update(b)
print(a)
