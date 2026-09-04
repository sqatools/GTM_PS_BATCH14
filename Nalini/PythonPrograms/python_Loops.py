"""
# print numbers from 1 to 10
# range function  range( start value, and value ,step)

for i in range(1, 10, 1):

    print("values between 1 to 10:", i)
"""
num = int(input("Enter a number: "))

primecount = 0

for i in range(1, num + 1):
    if num % i == 0:
        primecount += 1

if primecount == 2:
    print("Given number is prime")
else:
    print("Given number is not prime")











