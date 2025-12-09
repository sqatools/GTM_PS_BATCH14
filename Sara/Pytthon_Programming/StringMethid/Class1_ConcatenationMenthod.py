s1="Python"
s2="We are Learning Python programming"
s3="""
Regular exercise is essential for maintaining good health. It helps to control weight,
reduces the risk of chronic diseases, and improves mental health.
"""
print(s1)
print("-"*40)
print(s2)
print("-"*40)
print(s3)

print("String at index 4 of s2 is:",s2[4]) #String at index 4 of s2 is: r
print("String at index -15 of s3 is:",s3[-15]) #String at index -15 of s3 is: m

# Getting index value using char- index method
print("-"*15,"Index Method", "-"*15)

print("Index walue of Python Y is :", s1.index('y')) #Index walue of Python Y is : 1

print("-"*50)
#*********String Formatting Method***************

print("-"*15,"Concatenation Format using defined values","-"*15)
a1="Sam"
a2= 25
print("My name is "+a1+". My age is "+str(a2))

print("-"*15,"Concatenation Format using user provided values","-"*15)

e1=str(input("Please enter your name:"))
e2= int(input("Please enter your age:"))
print("My name is "+e1+". My age is "+str(e2))


