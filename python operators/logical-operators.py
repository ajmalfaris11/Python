# PYTHON LOGICAL OPERATORS
# *************************

#'  and   -> Logical AND      -> Returns True if both conditions are True
#'  or    -> Logical OR       -> Returns True if at least one condition is True
#'  not   -> Logical NOT      -> Reverses the result of a condition (True becomes False, and vice versa)



# PYTHON LOGICAL OPERATORS EXAMPLES
# **********************************

# LOGICAL AND EXAMPLE
# --------------------
a = 10
b = 20
c = 30
print("Logical AND: (a < b) and (b < c) ->", (a < b) and (b < c))  # True

# LOGICAL OR EXAMPLE
# -------------------
a = 10
b = 20
c = 5
print("Logical OR: (a < b) or (b < c) ->", (a < b) or (b < c))  # True

# LOGICAL NOT EXAMPLE
# --------------------
a = 10
b = 20
print("Logical NOT: not(a > b) ->", not(a > b))  # True
