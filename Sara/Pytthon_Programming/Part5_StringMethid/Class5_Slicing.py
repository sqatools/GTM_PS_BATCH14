#******Slicing Method****************
print("-"*15,"Slicing","-"*15)

w1="Hello! How are you?"
print(w1) #Hello! How are you?
print(w1[0:19]) #Hello! How are you?
print(w1[1:7:1]) #ello!
print(w1[-1:-5:-1]) # ?uoy
print(w1[-1:-5:1]) # emtpy string
print(w1[::]) #Hello! How are you?
print(w1[::-1]) #?uoy era woH !olleH
print(w1[0::1]) # Hello! How are you?
print(w1[-1::-1]) #?uoy era woH !olleH
print(w1[7::-1]) #H !olleH
print(w1[-7::-1]) #ra woH !olleH

# Homework slicing
print("-"*15,"Homework slicing","-"*15)
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"

# output2 = "airat is Best Batsman of IndiV"
a1=str3[0:1]
a2=str3[-1::1]
a3=(str3[1:-1:1])
print("Output 2: "+a2+a3+a1) # Output 2: airat is Best Batsman of IndiV

#****************************************************************************


print()
# output3 = "tiraV si tesB natsmaB fo andiI"
b1="Virat"
b2="is"
b3="Best"
b4="Batsman"
b5="of"
b6="India"
output3=b1[-1:-2:-1]+b1[1:4:1]+b1[:1:1]+" "+b2[::-1]+" "+b3[::-1]+" "+b4[-1:-2:-1]+b4[1:6:1]+b4[:1:1]+" "+b5[::-1]+" "+b6[-1:-2:-1]+b6[1:4:]+b6[:1:1]
print("Output 3: ",output3) #Output 3:  tiraV si tseB natsmaB fo andiI