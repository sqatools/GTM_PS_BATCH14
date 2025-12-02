########################### continue and break statement #############
# continue statement: when the continue condition is satisfied then it will move loop to next interation
# without executing the remaining code.
# print values from 1 to 10 with continue statement skip iteration 4 and 9
num =1
while num <=10:
    if num ==4 or num==9:
        num += 1
        continue

    print(num)
    num += 1

print()

# write a python program to check given number is prime or not
num2 = int(input("Enter your value : "))
count = 0
for i in range(2, num2): # 2
    print(i)
    if num2%i ==0:
        count += 1
        break
    else:
        continue

if count > 0:
    print("It is not a prime number", num2)
else:
    print("It is a prime number", num2)