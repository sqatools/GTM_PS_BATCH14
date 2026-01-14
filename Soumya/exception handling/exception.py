#exception handling---when an error ocuurance, normL flow of the progam wil disrupted to handle wil usethe exeception
from logging import exception


def addition(n1, n2):
    try:
        output = n1 + n2
        print(output)

    except Exception as e:
        print("Error: Both inputs must be numbers.")
        print("Exception message:", e)

addition(10, 20)  # Valid input
addition(10, '20')  # Invalid input, will raise TypeError
print("program continue")

# try and except block and else block

print("_"*25)
def add(m1,m2):
    try:
        output = m1 + m2
        print(output)
    except TypeError as a:
        print(a)
    else:
        print("both numbers are same type")

add(10, 20)
add(10, "20")
print("program continue")

# try and except block and else block and finally block

print("_"*25)
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
print("program continue")

#try and finally block

print("_"*25)
def division(n1, n2):
    try:
        result = n1 / n2
        print(result)
    finally:
        print("finally block :Division result:", result)
division(10, 0)




