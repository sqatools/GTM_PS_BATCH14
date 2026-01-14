print("hi")
"""
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
"""
print("----"*50)
name1="V"
name2="i"
name3="B"
name4="B"
name5="o"
name6="I"
str3 = "Virat is Best Batsman of India"
str4 = f"{name1}Virat {name2}is {name3}Best {name4}Batsman {name5}of {name6}India"
print(str4)

print("----"*50)
"""
str3 = "Virat is Best Batsman of India"

output2 = "airat is Best Batsman of IndiV"
"""
name7=""
name8="V"
str5 = "Virat is Best Batsman of India"
str6=print(str5[1:-1]) #airat is Best Batsman of Indiv
print(type(str6))
output2 = ('a' + str3[1:-1].replace('V', '').replace('a', '')) + 'V'
print(output2)  # airat is Best Batsman of IndiV
print(str3[1:-1].replace('V', '').replace('a',''))
print(str3)

print("----"*50)
"""
str3 = "Virat is Best Batsman of India"

# output3 = "tiraV si tesB natsmaB fo andiI"
"""
str6 = "Virat is Best Batsman of India"
print(str6[::-1])
print(str6.split(" "))
str7=str6.split(" ")
print(str7, type(str7))
print(reverse(str7))
