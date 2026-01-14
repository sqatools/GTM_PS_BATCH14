#####
# 1). Python Program to add two integer values.
num1 = 3
num2 = 5
print("two integer values are :", num1 + num2) # 8


# 2)Python Program to subtract two integer values.
print(num1 - num2)


print("_"*60)
# 3)Python program to multiply two numbers
print(num1 * num2)

print("_"*60)
# 4)Python program to repeat a given string 5 times.
# Input :
# str1 = “SQATools”
# Output :
# “SQAToolsSQAToolsSQAToolsSQAToolsSQATools”

str1 = "SQATools"
print(str1*5)

print("")
####5) Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number
####Input:
a = 40
b = 50
c = 30
# Output :
# Average = 40

print("Average of given numbers :", (a+b+c)/3)

print("_"*60)
#6). Python program to get the median of given numbers.
#Note: all the numbers should be arranged in ascending order
#Formula : (n+1)/2
#n = Number of values
#Input : [45, 60, 61, 66, 70, 77, 80]
#Output:  66

val = [45, 60, 61, 66, 70, 77, 80]
val.sort()
print(val)
n=len(val)
print(n)
if n%2==1:
    median_value = val[n // 2]
    print(n//2)
else:
    median_value = (val[n // 2 - 1] + val[n // 2]) / 2

print(f"The median is: {median_value}")

print("_"*60)
#7). Python program to print the square and cube of a given number.
#Input :
#num1 = 9
#Output :
#Square = 81
#Cube =   729

num = 9
print(num**2)
print(num**3)

print("_"*50)
#8). Python program to interchange values between variables.
#Input :
#a = 10
#b = 20
#Output :
#a = 20
#b = 10

a = 50
b = 70
a, b = b, a
print("value of a :", a)
print("value of b :", b)


print("_"*50)
#9). Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)


numm = int(input("Enter a number: "))
if numm % 2 == 0:
    print("even number")
else:
    print("odd number")

for i in range(1,30):
    if i % 3 ==0 :
        print(i)
    else :
        continue

print("_"*50)
marks = int(input("Enter marks : "))
if marks<40:
    print("failed")
elif marks>=40 and marks>=50:
    # marks is greater than 40 and less than 50 then got C grade.
    print("Grade C")
elif marks>50 and marks<=60:
    #  marks is greater than 50 and less than 60 then got B grade.
    print("Grade B")
elif marks>60 and marks<=70:
    #  marks is greater than 60 and less than 70 then got A grade.
    print("Grade A")
elif marks>70 and marks<=80:
    #  marks is greater than 70 and less than 80 then got A+ grade.
    print("Grade A+")
elif marks>80 and marks<=90:
    #  marks is greater than 80 and less than 90 then got A++ grade.
    print("Grade A++")
elif marks>90 and marks<=100:
    #  marks is greater than 90 and less than 100 then got Excellent grade.
    print("Excellent")
else:
    # marks is greater than 100 than consider as invalid number..
    print("Invalid marks")








