"""
Properties:
-> String is immutable data type, can not update the value.
-> We can define string with single quote, double quote, triple quote.
-> String follow positive negative indexing for each character in the string.
-> There is no specific limit to define the string.
"""

'''P  y  t  h  o  n'
   0  1  2  3  4  5  positive indexing starts with 0
  -6 -5 -4 -3 -2 -1  negative indexing starts with -1'''

str1 = 'Python'
print(str1)
print(type(str1))
print (str1[0])
print(str1[-4])
print("Index of y: ", str1.index('y'))#1



print("_"*10)
str1 = 'Hema'
print(str1)
print("_"*10)

str2 = "My name is Hema."
print(str2)
print("_"*10)

str3 = """My name is Hema. I live in Switzerland. I am basically from Pune, India."""
print(str3)
print("_"*10)

str4 = '''My name is Hema. I live in Switzerland. I am basically from Pune, India.'''
print(str4)
print("_"*10)

name = "Aayush"
age= 10
address ="Switzerland"

# 1. string concatenation:
Result1 = "My name is " + name + " and I am " + str(age) + "years old. " + "I live in " + address
print(Result1)
# 2. string format method:
Result2= "My name is {} and I am {}years old. I live in {}".format(name, age, address)
print(Result2)
# 3. f string formatting:
Result3 = f"My name is {name} and I am {age}years old. I live in {address}"
print(Result3)