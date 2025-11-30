##simple If
a=10
b=20
if a==b:
    print("print A: ",a)
else:
    print("print B: ", b)

#program to check if number is odd/even
n=12
if n%2==0:
    print (n,"is even")
else:
    print(n,"is odd")


#if-elif-if
n=40
x=20
y=30
z=40
if x==n:
    print("x is equal to n")
elif y==n:
    print("y is equal to n")
elif z==n:
    print("z is equal to n")
else:
    print("nothing matches n")


#nested If
day1= "sun"
day2= "mo"
day3= "tue"

if day1=="sun":
    print ("Day is sunday")
    if day2=="mon":
        print ("Day is monday")
        if day3=="tue":
            print("Day is tuesday")
        else:
            print("Day is NOT tuesday")
    else:
        print("Day is NOT monday")
else:
    print("Day is NOT sunday ")