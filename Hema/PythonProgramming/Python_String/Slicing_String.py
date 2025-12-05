# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"

print(str3[0]+str3[0:5]+" "+str3[6]+str3[6:8]+ " "+str3[9]+str3[9:14]+" "+str3[14]+str3[14:21]
      +" "+str3[22]+str3[22:25]+" "+str3[25]+str3[25:31])