# 1). Python program to check given number is divided by 3 or not.
print("# First Program" * 5)
num = 12
if num % 3 == 0:
    print("Value is divisible")
else:
    print("Value is not divisible")

# 2). If else program to get all the numbers divided by 3 from 1 to 30.
print("# Second Program" * 5)
for list2 in range(1, 31):
    if list2 % 3 == 0:
        print(list2, "divide by 3")
else:
    print(list2, "not divide by 3")

# 3). If else program to assign grades as per total marks.
print("# Third Program" * 5)
marks = int(input("Enter Marks: "))
if marks <= 40:
    print("Fail")
elif 40 < marks <= 50:
    print("grade C")
elif 50 < marks <= 50:
    print("grade B")
elif 60 < marks <= 70:
    print("grade A")
elif 70 < marks <= 80:
    print("grade A+")
elif 80 < marks <= 90:
    print("grade A++")
elif 90 < marks <= 100:
    print("Excellent")
elif marks > 100:
    print("Invalid marks")

# 4). Python program to check the given number divided by 3 and 5.
print("# 4th Program" * 5)
pnum = 45
if pnum % 3 == 0 and pnum % 5 == 0:
    print("Divided by both 3 and 5")
else:
    print("Not Divided")

# 5). Python program to print the square of the number if it is divided by 11.
print("# 5th Program" * 5)
num = 11
if num ** 2 % 11 == 0:
    print("Divided by 11")
else:
    print("Not Divided by 11")

# 6). Python program to check given number is a prime number or not.
print("# 6th Program" * 5)
num1 = int(input("Enter num1: "))
if num1 > 1:
    for i in range(2, num1):
        if num1 % i == 0:
            print(num1, "is Not Prime")
        else:
            print(num1, "is Prime")
else:
    print(num1, "is not prime")

# 7). Python program to check given number is odd or even.
print("# 7th Program" * 5)
num2 = int(input("Enter num2: "))
if num2 % 2 == 0:
    print(num2, "is Even")
else:
    print(num2, "is Odd")

# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
print("# 8th Program" * 5)
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num3 = int(input("Enter num3: "))
if num3 in fib:
    print(num3, "is part")
else:
    print(num3, "is not part")

#9). Python program to check authentication with the given username and password.
print("# 9th Program" * 5)
username = input("Enter name")
password = input("Enter password")
if username == password:
    print("username and password are valid")
else:
    print("username and password are not valid")

# 10). Python program to validate user_id in the list of user_ids.
print("# 10th Program" * 5)
user_id = ["a1", "b1", "c1", "d1"]
val = input("Enter user_id")
if val in user_id:
    print("value is in user_id")
else:
    print("not valid user_id")