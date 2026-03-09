#Exception handling is used to continue the program without interruption.

# 1. try except block
"""def addition(n1, n2):
    try:
        result = n1 + n2
        print("addition:", result)

    #except Exception as e:
    except TypeError as e:
        print("Error: Both inputs should be numbers")
        print("Exception details:", e)

addition(10, 20)

print("-"*10)
addition( 10, "30")# invalid input"""

# 2. try except else block
def divide(n1, n2):
    try:
        result = n1/n2
        print("addition:", result)

    except Exception as e:
        print("Error: Division by zero is not wllowed")
        print("Exception details:", e)

    else:
        print("Division result: ", result)

divide(10, 0)

print("-"*10)


