# Addition of two numbers
num1 = int(input("Enter Number1: "))

num2 = int(input("Enter Number2: "))


print("Addition of two numbers: ",num1+num2)

print("="*30)
# Subtraction of two numbers
num1 = 199
num2 = 30

print("Subtraction answer is:", num1-num2)
print("="*30)

# Multiplication of two numbers
num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2:"))
print("Multiplication answer is:", num1*num2)

print("="*30)

# Repeat given string 5 times
str1= input("Enter String: ")
print(str1*5)

print("="*30)

#Python program to get the Average of given numbers
total = 0
for i in range(5):
    num = int(input("Enter Number: "))
    total = total + num

avg = total/5
print("Average is:", avg)

print("="*30)

#Python program to get the median of given numbers.
list = [40,12,10,85,14,96]
list.sort();
n = len(list)
median = 0
if n % 2 == 0:
    median = (list[n//2 - 1] + list[n//2]) / 2
else:
    median = list[n//2]
print("Median is:", median)

print("="*30)

#Python program to print the square and cube of a given number.
num1 = int(input("Enter Number: "))
print("Square: ", num1 ** 2)
print("cube: ", num1 ** 3)




             