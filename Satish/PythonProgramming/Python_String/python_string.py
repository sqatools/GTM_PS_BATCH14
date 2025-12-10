# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"

str3_1=str3[0:5]
str3_11='V'+str3_1+'t'
str3_2=str3[6:8]
str3_22='i'+str3_2+'s'
str3_3=str3[9:13]
str3_33='B'+str3_3+'t'
str3_4=str3[14:21]
str3_44='B'+str3_4 +'n'
str3_5=str3[22:24]
str3_55='o'+str3_5 +'f'
str3_6=str3[25:30]
str3_66='I'+str3_6 +'a'
print(str3_11+" "+str3_22+" " +str3_33+" "+str3_44+" "+str3_55+" "+str3_66)


str3_a1=str3[1:5]
str3_a11='a'+str3_a1

str3_b1=str3[25:29]
str3_b11=str3_b1+'V'

str3_c1=str3[6:24]
print(str3_a11+" "+ str3_c1+ " "+str3_b11)

print("_"*50)
print(str3[-1:-6:-1])