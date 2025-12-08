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

# 9). Python program to check authentication with the given username and password.
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

# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively
print("# 11th Program" * 5)
n = 15
if n % 2 == 0:
    print("square is : ", n ** 2)
elif n % 3 == 0:
    print("cube is :", n ** 3)
else:
    print("invalid number")

# 12). Python program to describe the interview process.
print("# 12th Program" * 5)
exam_result1 = "passed"
exam_result2 = "failed"
if exam_result1 == "passed":
    print("first exam has been cleared")
    if exam_result2 == "passed":
        print("second exam has been cleared")
    else:
        print("Failed in 2nd exam")
else:
    print("Failed in 1st exam")

# 13). Python program to determine whether a given number is available in the list of numbers or not.
print("# 13th Program" * 5)
n1 = int(input("Enter the number:"))
list3 = [1, 23, "hi", 89 + 9j, (1, 6, 8), ('a', 'b'), {"a": 1, "b": 6}]
if n1 in list3:
    print(n1, "is in the list")
else:
    print(n1, "is not in list")

    # 14). Python program to find the largest number among three numbers.
    print("# 14th Program" * 5)
    a1 = int(input("Enter the a1 :"))
    a2 = int(input("Enter the a2 :"))
    a3 = int(input("Enter the a3 :"))
    if a1 > a2:
        if a1 > a3:
            print(a1, "is largest")
        else:
            print(a3, "is largest")
    elif a2 > a3:
        print(a2, "is largest")
    else:
        print(a3, "is largest")

# 15). Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible
print("# 15th Program" * 5)
age = int(input("Enter the age :"))
if age >= 18:
    print("Person is eligible")
else:
    print("Person is not eligible")

# 16). Python program to check whether any given number is a palindrome.
# Input: 121
# Output: palindrome
# 17). Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
# output = palindrome

# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# Input = Enter marks: 45
# Output = Pass
print("# 18th Program" * 5)
mark = int(input("Enter the mark :"))
if mark > 35:
    print("Pass")
else:
    print("Failed")

# 19). Python program to check whether the given number is positive or not.
# Input = 20
# Output = True
print("# 19th Program" * 5)
number = int(input("Enter the number :"))
if number > 0:
    print("Positive number")
else:
    print("Negative number")

# 20). Python program to check whether the given number is negative or not.
# Input = -45
# Output = True
print("# 20th Program" * 5)
number1 = int(input("Enter the number1 :"))
if number1 < 0:
    print("Negative number")
else:
    print("Positive number")

# 21). Python program to check whether the given number is positive or negative and even or odd.
# Input = 26
# Output = The given number is positive and even
print("# 21th Program" * 5)
number2 = int(input("Enter the number2 :"))
if number2 > 0:
    if number2 % 2 == 0:
        print("Positive and Even number")
    else:
        print("Positive and Odd number")
else:
    if number2 % 2 == 0:
        print("Negative and Even number")
    else:
        print("Negative and Odd number")

# 22). Python program to print the largest number from two numbers.
# Input:
# 25, 63
# Output = 63

print("# 22nd Program" * 5)
num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))
if num1 > num2:
    print(num1, " is largest")
else:
    print(num2, " is largest")

# 23). Python program to check whether a given character is uppercase or not.
# Input = A
# Output = The given character is an Uppercase

print("# 22nd Program" * 5)
input = input("Enter input: ")
if input in range("A-Z"):
    print(input, "is uppercase")
else:
    print(input, "is lowercase")