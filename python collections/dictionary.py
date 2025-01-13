# Dictionary Operations
# ***********************

# A dictionary is created using curly braces {} with key-value pairs
# Keys must be unique, and values can be of any data type

# Initialize a dictionary
dict1 = {
    "name": "Ajmal",
    "age": 20,
    "city": "Kochi",
    "profession": "Software Developer"
}

# Print the entire dictionary
print("Original Dictionary:", dict1)

# Access a value using a key
print("Name:", dict1["name"])

# Check if a key exists in the dictionary
if "age" in dict1:
    print("'age' is a key in the dictionary.")

# Add or update a key-value pair
dict1["country"] = "India"
print("After adding 'country':", dict1)

# Update the value of an existing key
dict1["age"] = 22
print("After updating 'age':", dict1)

# Remove an item using pop() (returns the value of the removed item)
removed_value = dict1.pop("city")
print("Removed 'city' with value:", removed_value)
print("After popping 'city':", dict1)

# Remove an item using popitem() (removes and returns the last added item)
removed_item = dict1.popitem()
print("Popped item:", removed_item)
print("Dictionary after popitem:", dict1)

# Get a value using get() (returns None if the key is not found, no error)
profession = dict1.get("profession", "Key not found")
print("Profession:", profession)

# Iterate through the dictionary and print each key-value pair
print("Items in the dictionary:")
for key, value in dict1.items():
    print(key, ":", value)


# Create another dictionary for comparison
dict2 = {
    "name": "Bilal",
    "age": 24,
    "city": "Kochi"
} 

# Merge two dictionaries using update() (updates dict1 with key-value pairs from dict2)
dict1.update(dict2)
print("After merging dict2 into dict1:", dict1)

# Copy the dictionary (creates a shallow copy)
dict3 = dict1.copy()
print("Copy of dict1:", dict3)

# Clear all items from the dictionary
dict1.clear()
print("Dictionary after clearing all items:", dict1)

# Delete the dictionary completely
del dict2
# Note: Accessing 'dict2' after this will raise an error
print("Dictionary deleted successfully.")  # Uncomment to confirm deletion
