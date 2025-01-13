# SET DATA COLLECTION
# *********************

# Sets are created using curly braces {}
# Sets are unordered, meaning they do not maintain the insertion order
# Sets do not allow duplicate values
# Sets are mutable, but their items must be immutable (e.g., numbers, strings, tuples)

# Initialize a set
set1 = {"Ajmal", "Nibras", "Fasil", "Zain", "Selman"}

# Print the entire set
print("Original Set:", set1)

# Check the number of items in the set
print("Number of items in the set:", len(set1))

# Add a single item to the set
set1.add("Shabeer")
print("After adding 'Ashraf':", set1)

# Add multiple items to the set using update()
set1.update(["Bilal", "Samrood"])
print("After adding multiple items:", set1)

# Check if an item exists in the set
if "Fasil" in set1:
    print("'Fasil' is in the set.")

# Remove an item using remove() (raises an error if the item is not found)
set1.remove("Zain")
print("After removing 'Zain':", set1)

# Remove an item using discard() (does not raise an error if the item is not found)
set1.discard("Selman")
print("After discarding 'Selman':", set1)

# Pop a random item from the set (sets are unordered, so the item is arbitrary)
popped_item = set1.pop()
print("Popped item:", popped_item)
print("Set after popping an item:", set1)

# Iterate through the set and print each item
print("Items in the set:")
for item in set1:
    print(item)


# Union of two sets (combines items from both sets, removing duplicates)
set2 = {"Faris", "Safdar", "Nibras"}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of two sets (common items)
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference of two sets (items in set1 but not in set2)
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

# Symmetric difference (items in either set1 or set2, but not in both)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# Clear all items from the set
set1.clear()
print("Set after clearing all items:", set1)

# Delete the set completely
del set1
# Note: Accessing 'set1' after this will raise an error
print("Set deleted successfully.")  # Uncomment to confirm deletion
