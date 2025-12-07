# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"

print("Output3:")
#Output 3 :"tiraV si tesB natsmaB fo andiI"
a= "Virat"
b= "is"
c= "Best"
d= "Batsman"
e= "of"
f= "India"

print(a[::-1],b[::-1],c[::-1],d[::-1],e[::-1],f[::-1])

print("X"*30)
print("Output2:")
S= "Virat is Best Batsman of India"
# Output2 = "airat is Best Batsman of IndiV"

Output2= f"{S[-1]}{a[1:]} {b} {c} {d} {e} {f[:3]} {a[0]}"
print(Output2)

print("X"*30)
print("Output1:")
#output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"

print(a[0]+a+a[4])
#print(+b[0]+b+b[1],+c[0]+c+c[3],+d[0]+d+d[6],+e[0]+e+e[1],f[0]+f+f[4])
Output1= f"{a[0]+a+a[4]} {b[0]+b+b[1]}"
print(Output1)



