str1 = 'abc'
str2 = "xyz"
str3 = '''qwer'''

print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))

print("_"*50)

str_a = "Python"
print(str_a[0])
print(str_a[-4])
print("_"*50)


name = "sumeet"
age = 30
city = "oslo"

#String concatination(use +)
result = "My name is "+name+" and my age is "+str(age)+" and i live in "+city
print(result)

#string format method(.format{}) - No need to convert number to string
result1 = "My name is {} and age is {} and i live in {}".format(name, age, city)
print("format result is ", result1)

#f string formatting
result3 = f"My name is {name} and age is {age} and city is {city}"
print(result3)




