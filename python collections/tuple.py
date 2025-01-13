# TUPLE DATA COLLECTION
# *********************

# Tuples are created using round brackets ()
# Tuples are immutable, meaning their values cannot be changed after creation
# Tuples can store duplicate items and support indexing like lists

# Initialize a tuple
tuple1 = ("Ajmal", "Nibras", "Fasil", "Zain", "Selman")

# Print the entire tuple
print("Original Tuple:", tuple1)

# Access a specific tuple element by index
print("Second item in the tuple:", tuple1[1])

# Get the number of elements in the tuple
print("Number of items in the tuple:", len(tuple1))

# Iterate through the tuple and print each item
print("Items in the tuple:")
for item in tuple1:
    print(item)

# Check if an item exists in the tuple
if "Fasil" in tuple1:
    print("'Fasil' is in the tuple.")

# Access a range of items in the tuple (slicing)
print("First three items in the tuple:", tuple1[:3])

# Concatenate two tuples
tuple2 = ("Shabeer", "Bilal")
combined_tuple = tuple1 + tuple2
print("Combined tuple:", combined_tuple)

# Repeat a tuple multiple times
repeated_tuple = tuple1 * 2
print("Repeated tuple:", repeated_tuple)

# Find the index of a specific item
item_index = tuple1.index("Zain")
print("Index of 'Zain':", item_index)

# Count the occurrences of a specific item
item_count = tuple1.count("Ajmal")
print("Count of 'Ajmal':", item_count)

# Convert a tuple to a list (to allow modification)
list_from_tuple = list(tuple1)
print("Tuple converted to list:", list_from_tuple)

# Convert the list back to a tuple
modified_tuple = tuple(list_from_tuple)
print("List converted back to tuple:", modified_tuple)

# Delete the tuple (completely removes it from memory)
del tuple1


# Note: After deleting, attempting to access 'tuple1' will raise an error
print("Tuple deleted successfully.")  # Uncomment this after confirming deletion
