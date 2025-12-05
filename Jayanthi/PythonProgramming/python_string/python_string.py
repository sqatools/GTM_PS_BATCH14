# String formating
"""name = input("Enter the name ")
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

#r raw string format
str_b = r"Hello \t\t we are \n Learning Python"
print(str_b)
"""

# Rule1 : str[start index:  end index]

"""str1="Python Programming"
print(str1[:])
print(str1[:11])
print(str1[11:15])
print(str1[0:18])
print(str1[11:-1])
print(str1[-11:-1])"""

"""# Rule2 : str[start index:  end index: step value]
str2="Learning python is fun"
print(str2[::])
print(str2[:-5:-1])
print(str2[::-1])
print(str2[::1])
print(str2[5:-1:1])
print(str2[-11:15:1])
print(str2[-11:5:-1])"""

# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"

print(str3[0:1]+str3[0:5]+str3[4:6]+str3[6:7]+str3[6:8]+str3[7:9]+str3[9:10]+str3[9:13]+str3[12:14]
      +str3[14:15]+str3[14:21]+str3[20:22]
      +str3[22:23]+str3[22:24]+str3[23:25]+str3[25:26]+str3[25:30]+str3[29:30])
print(str3[29:30]+str3[1:29]+str3[0:1])
print(str3[4::-1]+str3[8:5:-1]+str3[13:8:-1]+str3[21:13:-1]+str3[24:20:-1]+str3[29:24:-1])