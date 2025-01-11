# String Basics
# *************

text1 = 'Hello World'  # Single quotes
text2 = "Hello Python"  # Double quotes

# Triple Quotes for Writing Multiline Text
text3 = """ 
This is Multiple Line text 
using triple quotes 
"""

print(text1)
print(text2[1])       # Strings work like arrays; access value by index
print(text2[0:5])     # Access a specific range of characters using slicing

# String Methods
# **************

# 1. Length of a String: len()
print("\n1. Length of String:")
print(len(text1))  # Output: 11

# 2. Remove Unwanted Space: strip(), lstrip(), rstrip()
print("\n2. Remove Unwanted Space:")
text = "   Hello, World!   "
print(text.strip())  # Removes spaces from both ends
print(text.lstrip()) # Removes spaces from the left
print(text.rstrip()) # Removes spaces from the right

# 3. Case Conversion: lower(), upper(), title(), capitalize()
print("\n3. Case Conversion:")
text = 'HELLO WORLD!'
print(text.lower())      # Convert to lowercase
text = 'hello world!'
print(text.upper())      # Convert to uppercase
text = 'hello world!'
print(text.title())      # Convert to title case
text = 'hello world!'
print(text.capitalize()) # Capitalize the first character only

# 4. Replace Text: replace()
print("\n4. Replace Text:")
text = "how's it?"
print(text.replace("it", "that"))  # Replace "it" with "that"

# 5. Join Strings: + operator, join()
print("\n5. Join Strings:")
text1 = "Hello "
text2 = "Ajmal!"
fText = text1 + text2  # Using `+` operator
print(fText)
# Using `join()` method
words = ["Hello", "Ajmal!"]
print(" ".join(words))  # Join with space

# 6. Format Text: format(), f-strings
print("\n6. Format Text:")
name = "Ajmal"
age = 20
text = "My name is {}, I am {} years old"
print(text.format(name, age))  # Using `format()`
# Using f-strings (Python 3.6+)
print(f"My name is {name}, I am {age} years old")

# 7. String Splitting: split(), rsplit(), splitlines()
print("\n7. String Splitting:")
text = "apple,banana,cherry"
print(text.split(","))  # Split by comma
print(text.rsplit(",", 1))  # Split by the last comma (max 1 split)
text = "Line1\nLine2\nLine3"
print(text.splitlines())  # Split into lines

# 8. String Searching: find(), index(), startswith(), endswith()
print("\n8. String Searching:")
text = "Hello, welcome to the Python world."
print(text.find("welcome"))      # Find position of "welcome" (returns -1 if not found)
print(text.index("welcome"))     # Same as find but raises ValueError if not found
print(text.startswith("Hello"))  # Check if string starts with "Hello"
print(text.endswith("world."))   # Check if string ends with "world."

# 9. String Validation: isdigit(), isalpha(), isalnum(), isspace()
print("\n9. String Validation:")
text = "12345"
print(text.isdigit())  # True: All characters are digits
text = "Hello"
print(text.isalpha())  # True: All characters are alphabets
text = "Hello123"
print(text.isalnum())  # True: All characters are alphanumeric
text = "   "
print(text.isspace())  # True: All characters are spaces

# 10. Miscellaneous Methods
print("\n10. Miscellaneous Methods:")
text = "Hello, World!"
print(text.count("o"))         # Count occurrences of "o"
print(text.swapcase())         # Swap case of all letters
print(text.zfill(20))          # Pad string with zeros to a total length of 20
print(text.center(20, "*"))    # Center align with padding
print(text.ljust(20, "-"))     # Left align with padding
print(text.rjust(20, "-"))     # Right align with padding
