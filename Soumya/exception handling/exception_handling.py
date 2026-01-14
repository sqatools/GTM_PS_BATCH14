# exception handling : when an error occurs,
# the normal flow of the program is disrupted.
# To handle such situations, we use exception handling.

def addition(n1, n2):
    try:
        output = n1 + n2
        print(output)
    except Exception as e:
        print("Error: Both inputs must be numbers.")
        print("Exception message:", e)


#addition(10, 20)  # Valid input
#addition(10, '20')  # Invalid input, will raise TypeError
#print("Program continues...")

#########################################
# try and except block and else block

def divide(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        # This block executes if no exception occurs
        print("Division result:", result)


# divide(10, 2)  # Valid input
divide(10, 0)  # Division by zero

print("Program continues...")

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


#multiply(10, 5)  # Valid input
multiply(10, {'a': 123})  # Invalid input, will raise TypeError


print("##########################################")
# Raising exceptions manually
def check_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            
            print("You are a minor.")
        else:
            print("You are an adult.")
    except ValueError as ve:
        print("Error:", ve)


#check_age(20)  # Valid input
# check_age(-5)  # Invalid input, will raise ValueError
# Error: Age cannot be negative.

print("##########################################")
# Custom exception class
class NegativeAgeError(Exception):
    """Custom exception for negative age values."""
    pass

def validate_age(age):
    try:
        if age < 0:
            raise NegativeAgeError("Age cannot be negative.")
        else:
            print("Valid age:", age)
    except NegativeAgeError as nae:
        print("Custom Error:", nae)


# validate_age(25)  # Valid input
# Valid age: 25

validate_age(-10)  # Invalid input, will raise NegativeAgeError
# Custom Error: Age cannot be negative.


print("##########################################")
# multiple exceptions handling
def process_data(data):
    try:
        # Simulate processing data
        result = 100 / data['value']
        print("Processing result:", result)
    except KeyError as e:
        print("Error: Missing key in data -", e)
    except TypeError as e2:
        print("Error: Invalid data type -", e2)
    except ZeroDivisionError as e3:
        print("error: Division by zero -", e3)


# process_data({'value': 20})  # Valid input
# Processing result: 5.0

# process_data({'val': 20})  # Missing key, will raise KeyError
# Error: Missing key in data - 'value'

# process_data({'value': 0})  # Division by zero, will raise ZeroDivision
# error: Division by zero - division by zero

######################################################