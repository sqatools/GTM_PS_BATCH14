# *****************STRING FORMAT METHOD********************
print("-"*15,"format method: string conversion using hardcode value","-"*15)
print()
name="Dalia"
age= 22
r1= "My name is {} and my age is {}".format(name,age)
print("Format method result 1: ",r1)
print()

#*******************************************
print("-"*15,"format method: string conversion using user provided value","-"*15)
print()
name=str(input("Please enter your name:"))
age= int(input("Please enter your age"))
r1= "My name is {} and my age is {}".format(name,age)
print("Format method result 2: ",r1)