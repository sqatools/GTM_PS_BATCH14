# write a python program to check the given number is divisible by 3 and 5
n = input("Please enter your value here: ")
x = int(n)

if x % 3 == 0 and x % 5 == 0:
    print("Given number is divisible by 3 and 5")
else:
    print("Given number is not divisible by 3 and 5")

print("*"*50)
n = input("Please enter your value here:")
x = int(n)

if x % 3 ==0 or x % 5 ==0:
    print("Condition satisfied")
else:
    print("Condition not satisfied")

print("*"*50)
# write a program to accept the student marks and provides its result as marks obtained.

mark = int(input("Please enter your marks:"))
if mark <= 30:
    print("Sorry Please reappear")
elif mark > 30 and mark <= 40:
    print("You are grade 3")
elif mark > 40 and mark <=50:
    print("You are grade 2")
elif mark > 50 and mark <= 60:
    print("You are grade 1")
elif mark >70 and mark<100:
    print("Good! you are outstanding :) ")
else:
    print("This is not valid mark!!!!!!!")

