# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"

#Output 3 :"tiraV si tesB natsmaB fo andiI"
a= "Virat"
b= "is"
c= "Best"
d= "Batsman"
e= "of"
f= "India"
g=0
print(a[::-1],b[::-1],c[::-1],d[::-1],e[::-1],f[::-1])

print("X"*30)
S= "Virat is Best Batsman of India"
# Output2 = "airat is Best Batsman of IndiV"

Output2= f"{S[29] +a[1:] +b +c +d +e+ f[:3]+a[0]}"
print (Output2)









