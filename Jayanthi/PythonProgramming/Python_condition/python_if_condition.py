#number are equal
a=50
b=100

print(a==b)

if a==b:
    print("Value a is equal to b")
else:
    print("Value a is equal to b")

# is the given number was even number
c=121
if c % 2 ==0:
    print("Given value is a even number")
else:
    print("Given number is a odd num")

n=30
x=40
y=60
z=50
if n==x:
    print("value of n and x equal")
elif n==y:
    print("value of n and y equal")
elif n==z:
    print("value of n and z equal")
else:
    print("no value matches")

round1="fail"
round2="pass"
round3="pass"
if round1=="pass":
    print("Round1 is cleared")
    if round2=="pass":
        print("Round2 is cleared")
        if round3=="pass":
            print("Round3 is cleared")
        else:
            print("Round3 is not cleared")
    else:
        print("Round2 is not cleared")
else:
    print("Round1 is not cleared")


# Logical operator
# and & or & !=
age=20
if age > 18 and age < 25:
    print("Eligible for the vote but less than 25 and greater than 18")

age=30
if age > 18 or age <25:
    print("Eligible for the vote but less than 25 or greater than 18")


is_raining=False
if not is_raining:
    print("Print go outside")

# Write a program to check the given number is divisible by 3 and 5

num1 = input("Please enter your value:")
print(num1,type(num1))
x=int(num1)

if x%3==0 and x%5==0:
    print("Divisible by 3 and 5")
else:
    print("not Divisible by 3 and 5")

# Write a program to check the given number is divisible by 3 or 5

if x%3==0 or x%5==0:
    print("Divisible by 3 or 5")
else:
    print("not Divisible by 3 or 5")

# write a program to accept the student marks and provides its result as marks obtained.

marks=int(input("Please enter the marks"))
if marks<=30:
    print("The candidate failed ")
elif 30 >= marks <=40:
    print("The candidate passed with 3rd class ")
elif marks > 40 and marks <= 50:
    print("The candidate passed with 2nd class ")
elif marks >50 and marks <= 60:
    print("The candidate passed with 1st class ")
elif marks >60 and marks <=100:
    print("The candidate passed with distinction ")
else:
    print("marks more than 100 is invalid")

# write a python program to check given value is available in list of values.
val=51
list1=[23,56.98,51,'python']
if val in list1:
    print(val, "is in the list")
else:
    print(val,"is not in list")

# write a python program to check given value is available # not in operator tuple of values.
val11=56
tup1=(56,63.98,'python',3+5j)
if val11 not in tup1:
    print(val11, "is in the tup")
else:
    print(val11,"is not in tup")

# write a python program to check given value is available  in operator dirc of values.

dist1={'a':125, 'b': 150,'c':"python"}
val10='a'
if val10 in dist1:
    print("the val is in the dist")
    print(dist1[val10],val10)
else:
    print("the value is not in dis")

# is operator

list5 = [5, 7, 8]
list6 = [5, 7, 8]
list7 = list5

# compare list1 with list2 using equal operator ==
if list5 == list6:
    print("Both are equal")
else:
    print("both are not equal")

if list5 is list6:
    print("Both are same")
else:
    print("both are not same")


if list7 is list6:
    print("Both are same")
else:
    print("both are not same")




