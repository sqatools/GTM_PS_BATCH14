# Function without parameter
def program():
    print("Hi")


# Function with parameter
def program_value(s):
    print(s)


# call by value:
print("call by value:")
program_value("Hello, user")

# call by reference
print("call by reference: ")
a = "Data for Python"
program_value(a)
