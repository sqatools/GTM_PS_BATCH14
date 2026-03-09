#1
"""
num=int(input("Enter any number:"))

if(num%3==0):
    print(num," is divisible by 3")
else:
    print(f"{num}"+" is not divisible by 3")
"""
#2
"""
for i in range(1,31):
    if(i%3==0):
        print(i," is divisible by 3")
    else:
        print(i," is not divisible by 3")
"""

#3

marks=int(input("Enter any marks:"))

if(marks<40):
    print("Fail")
elif(marks>=40 and marks<50):
    print("Grade c")
elif(marks>=50 and marks<60):
    print("Grade b")
elif(marks>=60 and marks<70):
    print("Grade a")
elif(marks>=70 and marks<80):
    print("Grade a+")
elif(marks>=80 and marks<90):
    print("Grade aa+")
elif(marks>=90 and marks<100):
    print("excellent")
else:
    print("you have to enter marks less than 100")

#4

#prime number
#num=int(input("Enter any number:"))
#count=0
#   if(num%i==0):
#       count+=1
#if(count>0):
 #   print("it is not a prime number")
#else:
 #   print("it is a prime number")

#5fibonaaci series
'''
num=int(input("Enter any number:"))
var1=0
var2=1
var3=var1+var2
print(var1) #0
print(var2) #1
list=[var1,var2]
for i in range(1,9):
    var3=var1+var2 #1
    print(var3)#1
    list.append(var3)
    var1=var2
    var2=var3

print(list)
if num in list:
    print("num is in fibonacci series")
else:
    print("num is not in fibonacci series")

#print(list)
'''