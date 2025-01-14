# Lambda Function == Anonymous Function
# Syntax ---> lambda arguments: expression

# Example of a Lambda Function:
# Creating a lambda function to calculate the square of a number
square = lambda x: x * x  # Lambda Function is defined using the `lambda` keyword

# Calling the lambda function
print(square(2))  # Output: 4


# Using `filter` with a normal function:

# A list of numbers to be filtered
list1 = [1, 2, 3, 4, 5, 6]

# Defining a normal function to check if a number is even
def even(x):
    if x % 2 == 0:  # Condition to check if the number is divisible by 2
        return x    # Return the number if it is even

# Using `filter` with the normal function to filter even numbers
f = filter(even, list1)

# Converting the filter object to a list and printing it
print(list(f))  # Output: [2, 4, 6]


# Using `filter` with a lambda function:

# Using `filter` with a lambda function to filter odd numbers
# The lambda function checks if a number is NOT divisible by 2 (odd)
od_filter = filter(lambda x: x % 2 != 0, list1)

# Converting the filter object to a list and printing it
print(list(od_filter))  # Output: [1, 3, 5]
