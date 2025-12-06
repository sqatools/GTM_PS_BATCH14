#INDEXING :
str2='python'
print("index of t",str2.index('t'))
#index method gives positive index only , not negative index


####string_formatting####

#expected output : My name is mona, age is 30, i live in BBSR
name="mona"
age=30
city="BBSR"
#string concatenation- u cant concatenate int with string hence str function is used
result1 = "My name is "+name+",age is "+str(age)+",i live in "+city
print("Result1:",result1)

#string_format_method
result2= "My name is {},age is {},i live in {}".format(name,age,city)

print("result2:", result2)

result3 =f"My name is {name},age is {age},i live in {city}"
print("result3:", result3)

