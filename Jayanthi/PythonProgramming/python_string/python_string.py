# String formating
name = input("Enter the name ")
age= int(input("Enter the age "))
city = input("Enter the city ")

#concat
result1="my name is "+name+" and my age "+str(age)+" living in "+city
print(result1)

#format method
result2="my name is {} and my age {} living in {}".format(name,age,city)
print(result2)

#f format method
result3=f"my name is {name} and my age {age} living in {city}"
print(result3)

