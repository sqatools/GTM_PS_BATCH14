# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"

print(str3[4::-1]+str3[8:5:-1]+str3[13:8:-1]+str3[21:13:-1]+str3[24:20:-1]+str3[29:24:-1])

print(str3[0:1]+str3[0:5]+str3[4:6]+str3[6:7]+str3[6:8]+str3[7:9]+str3[9:10]+str3[9:13]+str3[12:14]
      +str3[14:15]+str3[14:21]+str3[20:22]+str3[22:23]+str3[22:24]+str3[23:25]+str3[25:26]+str3[25:30]+str3[29:30])
print(str3[29:30]+str3[1:29]+str3[0:1])