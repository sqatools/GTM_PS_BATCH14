# Exception Handling in Python
# First Snippet: Handling exceptions using try and except block
def addition(a, b):
    try:
        sum_result = a + b
        print(f"The sum is: {sum_result}")
    except TypeError:
        print("Error: Both inputs must be numbers.")
addition(5, 10)  # Valid input
addition(5, '10')  # Invalid input, will raise TypeError

print("#########################################")
# same program with e variable to capture exception details
def addition(n1, n2):
    try:
        output = n1 + n2
        print(output)
    except Exception as e:
        print("Error: Both inputs must be numbers.")
        print("Exception message:", e)
addition(10, 20)  # Valid input
addition(10, '20')  # Invalid input, will raise TypeError

print("#########################################")
# try and except block and else block
def divide(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        # This block executes if no exception occurs
        print("Division result:", result)
divide(10, 2)  # Valid input
divide(10, 0)  # Division by zero

print("#########################################")
# try and except block and else block and finally block
def multiply(n1, n2):
    try:
        result = n1 * n2
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        # This block executes if no exception occurs
        print("else block :Multiplication result:", result)
    finally:
        # This block always executes
        print("finally block :Execution of multiply function is complete.") 
multiply(10, 5)  # Valid input
multiply(10, {'a': 123})  # Invalid input, will raise TypeError

print("##########################################")
# Raising exceptions manually   
def check_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        else:
            print(f"Your age is: {age}")
    except ValueError as ve:
        print("ValueError:", ve)
check_age(25)  # Valid age
check_age(-5)  # Invalid age, will raise ValueError

print("##########################################")
# custom exception class
class NegativeAgeError(Exception):  
    pass    
def validate_age(age):
    try:
        if age < 0:
            raise NegativeAgeError("Age cannot be negative.")
        else:
            print(f"Your age is: {age}")
    except NegativeAgeError as nae:
        print("NegativeAgeError:", nae)
validate_age(30)  # Valid age
validate_age(-10)  # Invalid age, will raise NegativeAgeError

print("##########################################")
# multiple exceptions handling
def process_number(num):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError("Input must be a number.")
        if num < 0:
            raise ValueError("Number cannot be negative.")
        result = num ** 0.5  # Calculate square root
    except TypeError as te:
        print("TypeError:", te)
    except ValueError as ve:
        print("ValueError:", ve)
    else:
        print(f"The square root of {num} is {result}")
process_number(16)  # Valid input
process_number(-4)  # Invalid input, will raise ValueError