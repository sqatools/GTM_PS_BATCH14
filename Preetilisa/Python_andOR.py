num1 = input("Please enter your value:")
# input accepts the values in string format only
print(num1, type(num1))
x = int(num1)

if x % 2 == 0 and x % 10 == 0:
    print("This number is divisible by 2 and 10 :", x)
else:
    print("This number is not divisible by 2 and 10:", x)
