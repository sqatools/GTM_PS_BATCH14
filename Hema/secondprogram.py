# write a python program to check the given number is divisible by 3 and 5

number1 = int(input("Enter the vale: "))
if number1 % 3 == 0 and number1 % 5 == 0:
    print("The number is divisible by 3 and 5", number1)
else:
    print("The number is not divisible by 3 and 5", number1)

number1 = int(input("Enter the vale: "))
if number1 % 3 == 0 or number1 % 5 == 0:
    print("The number is divisible by 3 and 5", number1)
else:
    print("The number is not divisible by 3 and 5", number1)
