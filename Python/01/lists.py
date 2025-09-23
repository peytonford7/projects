# Lists
users = ["Peyton", "Alex", "Jordan"]
print(users)

# Add new names
users.append("Taylor")
print(users)

users += ["Chris"]
print(users)

users.extend(["Sam", "Jamie"])
print(users)

# Insert at specific position
users.insert(1, "Morgan")
print(users)

# Insert without deleting
users[2:2] = ["Riley", "Casey"]
print(users)

# Replace values (insert with deletion)
users[1:3] = ["Dana", "Evan"]
print(users)

# Remove by index
del users[1]
print(users)

# Sort alphabetically
users.sort()
print(users)

print("\n")

# Numbers list
nums = [9, 90, 1, 2, 3, 6, 23]
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

print(sorted(nums, reverse=True))

# Copy nums list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
print(type(nums))

print("\n")

# Tuples
mytuple = ("Peyton", 23, True)
anothertuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# Change tupl
newlist = list(mytuple)
newlist.append("Student")
newtuple = tuple(newlist)
print(newtuple)
print(type(newtuple))

# Tuple unpacking
(one, two, *rest) = anothertuple
print(one)
print(two)
print(rest)

(one, *middle, last) = anothertuple
print(one)
print(middle)
print(last)

# Count occurrences
print(anothertuple.count(2))
