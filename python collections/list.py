# LIST DATA COLLECTION
# *********************

# Initialize the lists
list1 = ["Ajmal", "Nibras", "Fasil", "Zain", "Selman"]
list2 = [10, 20, 30, 40, 50]

# Print all the list items
print("Original List 1:", list1)

# Print a specific list item by index
print("Second item in List 1:", list1[1])

# Count the number of items in the list
print("Number of items in List 1:", len(list1))

# Perform calculation using items from list2
print("Sum of first and fourth items in List 2:", list2[0] + list2[3])

# Change the first item in the list
list1[0] = "Faris"
print("After changing the first item in List 1:", list1)

# Print each item in the list using a for loop
print("Items in List 1 after modification:")
for item in list1:
    print(item)

# Add an item to the end of the list
list1.append("Samrood")
print("After appending 'Samrood':", list1)

# Add an item at a specific position (index 5)
list1.insert(5, "Safdar")
print("After inserting 'Safdar' at index 5:", list1)

# Remove a specific item from the list
list1.remove("Faris")
print("After removing 'Faris':", list1)

# Remove all items from the list
list1.clear()
print("After clearing all items in List 1:", list1)

# Delete the list entirely
del list1

# Reinitialize the list for demonstration
list1 = ["Ajmal", "Nibras", "Fasil", "Zain", "Selman"]

# Extend a list by appending elements from another list
list1.extend(["Shabeer", "Bilal"])
print("After extending List 1 with new items:", list1)

# Remove an item by its index using pop
list1.pop(2)  # Removes the third item ("Fasil")
print("After popping the item at index 2:", list1)

# Reverse the order of the list
list1.reverse()
print("After reversing List 1:", list1)

# Sort the list alphabetically
list1.sort()
print("After sorting List 1:", list1)

# Copy the list to create a duplicate
list_copy = list1.copy()
print("Copied list:", list_copy)

# Check if an item exists in the list
if "Nibras" in list1:
    print("'Nibras' is in the list.")
else:
    print("'Nibras' is not in the list.")
