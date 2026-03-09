"""
Program to check if a number is divisible by 3 and 5.
"""

def check_divisibility():
    """
    Takes user input and checks divisibility by 3 and 5.
    """
    try:
        num = int(input("Enter a number: "))
        
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num} is divisible by both 3 and 5")
        else:
            if num % 3 == 0:
                print(f"{num} is divisible by 3 but not 5")
            elif num % 5 == 0:
                print(f"{num} is divisible by 5 but not 3")
            else:
                print(f"{num} is divisible by neither 3 nor 5")
                
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    check_divisibility()
