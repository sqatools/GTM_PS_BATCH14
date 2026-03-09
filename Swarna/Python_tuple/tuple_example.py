"""
Python Tuple Examples
---------------------
This script demonstrates various operations with Python tuples.
"""

# 1. Creating a Tuple
# Tuples are created using parentheses ()
fruits = ("apple", "banana", "cherry", "date")
print(f"Original Tuple: {fruits}")

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print(f"Mixed Tuple: {mixed_tuple}")

# Single element tuple (note the comma)
single_tuple = (5,)
print(f"Single element tuple type: {type(single_tuple)}")

# 2. Accessing Elements
# Access by index (0-based)
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Slicing
print(f"First two fruits: {fruits[:2]}")

# 3. Tuple Immutability
# Tuples cannot be changed after creation.
# The following line would raise a TypeError:
# fruits[0] = "orange" 

# 4. Tuple Methods
numbers = (1, 2, 3, 2, 4, 2)

# count(): Returns the number of times a value appears
count_of_twos = numbers.count(2)
print(f"Number of 2s in numbers tuple: {count_of_twos}")

# index(): Finds the first index of a value
index_of_three = numbers.index(3)
print(f"Index of value 3: {index_of_three}")

# 5. Tuple Unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Unpacked coordinates: x={x}, y={y}, z={z}")

# 6. Checking for existence
if "banana" in fruits:
    print("Yes, banana is in the fruits tuple")
