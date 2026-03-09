# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"

# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
print(str3[0]+str3[0:5]+" "+str3[6]+str3[6:8]+ " "+str3[9]+str3[9:14]+" "+str3[14]+str3[14:21]
      +" "+str3[22]+str3[22:25]+" "+str3[25]+str3[25:31])

# output2 = "airat is Best Batsman of IndiV"
print(len(str3))
print(str3[-1]+ str3[-29:] + str3[0])

# output3 = "tiraV si tesB natsmaB fo andiI"
print(str3[1:5]+str3[0] + " " +str3[7]+str3[6] + " "+ str3[10:13]+str3[9] + " "+ str3[15:21] + str3[14]
      +" " + str3[23]+str3[22]+ " "+ str3[26:]+str3[25])