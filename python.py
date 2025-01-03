# PRINTING BASIC CODES
# ---------------------

print("hello world") # print hello world
print(10+20) # print 10+20




# DATA TYPES & VARIABLES
#_________________________


# naming variables
#------------------
# 1 - starting with letter or underscore
# 2 - connot start with number
# 3 - Alphanumeric (A-z, 0-9, _)
# 4 - case sensitive (name, Name, NAME)
# 5 - no space between variable name
# 6 - no special characters (!, @, #, $, %, ^, &, *)
# 7 - no need to mention data type, just need to assign value

a = 10 # integer
print(a) # print a

name = "Ajmal" # string
print(name) # print name


# DATA TYPES :-
# -------------

# Numeric Types:-
a = 10 # Integer
number = 10.5 # Float
x = 10j # Complex

# Sequence Types:-
name = "Ajmal" # String
fruits = ["apple", "banana", "cherry"] # List
coordinates = (10, 20) # Tuple

# Text Type :-
name = "Hello World" # String

# Set Types :-
unique_numbers = {1, 2, 3} # Set
frozen_set = frozenset([1, 2, 3]) # Frozenset

# Mapping Type :-
person = {"name": "Ajmal", "age": 22}  # Dictionary

# Boolien Type :-
on = True # Boolean
off = False # Boolean

#  Binary Type :-
byte_data = b"Hello" # Bytes
byte_array = bytearray(5) # ByteArray
mem_view = memoryview(byte_array) # MemoryView

# None Type :-
no_value = None # None

# Check data type eg:-
print("printing person type :-", type(person))