#**************** f FORMAT METHOD *********************
print("-"*15,"f format method with hardcode value","-"*15)
print()
name="Vam"
age=27
city="Delhi"
r1= f"My name is {name} and my age is {age}. I am from {city}"
print("Result 1 using f format method: ",r1)
print()
#**************** f FORMAT METHOD *********************
print("-"*15,"f format method with usr provided value","-"*15)
print()
name=str(input("Please enter the name: "))
age= int(input("Please enter the age: "))
city= str(input("Please enter the city: "))
r1= f"My name is {name} and my age is {age}. I am from {city}"
print("Result 1 using f format method: ",r1)

