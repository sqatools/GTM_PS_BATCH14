"""
Properties:
-> String is immutable data type, can not update the value.
-> We can define string with single quote, double quote, triple quote.
-> String follow positive negative indexing for each character in the string.
-> There is no specific limit to define the string.
"""
str1 = 'Hello'
str2 = "We are learning Python"
str3 = '''
Zorzi is down on the ground clutching his right hamstring. 
He turned for the second run and immediately felt something, 
managed to hobble to the other end.
'''

str4 = """
He turned for the second run and immediately felt something,
 managed to hobble to the other end. This does not look good.
The physio is out there in the middle. de Zorzi is in a lot 
of pain. Meanwhile, Maharaj is ready near the rope 
"""

print(str1, type(str1))
print("_"*50)
print(str2, type(str2))
print("_"*50)
print(str3, type(str3))
print("_"*50)
print(str4, type(str4))
print("_"*50)


#################### string follows positive and negative indexing #######

str_a = "Python"

"""
 0  1  2  3  4  5   +ve indexing
 P  y  t  h  o  n
-6 -5 -4 -3 -2 -1   -ve indexing
"""

print(str_a[0])  # P
print(str_a[-3]) # h

print("index of t :", str_a.index('t')) # index of t : 2

print("_"*50)
################################## string formatting ####################

name = "Rahul"
age = 25
city = "Mumbai"

# name = input("Please enter username :")
# age = input("Please enter age:")  # "25"
# city = input("Please enter city name:")

# My name is Rahul and age is 25, I live in mumbai

# 1. string concatenation:
result1 = "My name is "+name+" and age is "+str(age)+", I live in "+city
print("Result1 :", result1)


# 2. string format method:
result2 = "My name is {} and age is {}, I live in {}".format(name, age, city)
print("Result2 :", result2)

# 3. f string formatting:
result3 = f"My name is {name} and age is {age}, I live in {city}"
print("Result3 :", result3)
print("88888"*30)
