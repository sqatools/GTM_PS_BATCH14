
def addition():

    try:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        print(f"doing addition... with {n1} and {n2}")
        output = n1 + n2
        print(output)
    except Exception as e:
        print("Error: Both inputs must be numbers.")
        print("Exception message:", e)

def substraction():
    try:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        print(f"doing substraction... with {n1} and {n2}")
        output = n1 - n2
        print(output)
    except Exception as e:
        print("Error: Both inputs must be numbers.")
        print("Exception message:", e)

## Why __name__ == "__main__": is used?
if __name__ == "__main__":
    while True:
        print("Choose operation:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            addition()
        elif choice == '2':
            substraction()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")


# print("Program first function call...")
# addition()  # Valid input
# print("Program second function call...")
# addition()  # Invalid input, will raise TypeError
# print("Program continues...")
# print("Program third function call...")
# substraction()  # Valid input



# def addition(n1, n2):
#     output = n1 + n2
#     print(output)
 
# print("Program first function call...")
# addition(10, 20)  # Valid input
# print("Program second function call...")
# addition(10, '20')  # Invalid input, will raise TypeError
# print("Program continues...")
