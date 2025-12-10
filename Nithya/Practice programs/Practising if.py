'''1). Python program to check given number is divided by 3 or not.'''
A=21
Reminder=(A%3)
if(Reminder==0):
    print("1. This is a multiple of 3:",A)
else:
    print("1. This is not a multiple of 3:",A)

'''If else program to get all the numbers divided by 3 from 1 to 30.'''
n=0
m=n+1
o=31
if (n%3==0):
    print ("n"),
elif (m==o):
    print("Values are displayed")
else:
        print("These are the numbers divisible by 3 between 1-30.")

'''If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks'''

marks=101

if marks<=40:
    print("Failed",marks)
elif marks>40 and marks<=50:
    print("Grade C",marks)
elif marks>=51 and marks<=100:
    print("Grade B",marks)
else :
    print("Invalid marks")

#####################
#Python program to check authentication with the given username and password.
'''
Username="Login"
Password="key123"
X= input("Enter your username:")
Y= input("Enter password:")
if X==Username and Y==Password:
    print("You have logged in successfully")
else:
    print("Username or Password is invalid")
'''
###############
print('#'*30)


# 10). Python program to validate user_id in the list of user_ids.

list=['logon', 'username','Access']

user_id= input('Enter the user_id')
if user_id in list:
    print("You are allowed")
else:
    print("Try again")


