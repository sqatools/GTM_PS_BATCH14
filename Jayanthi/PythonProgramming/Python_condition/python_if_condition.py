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
