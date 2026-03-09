str1 = "Python test"
str2 = """
Documentation for Python's standard library, along with tutorials and guides, are available online.
"""
print(str1, type(str1))
print(str2, type(str2))

print(str1[0])
print(str1[-4])
print(str2[3])
print(str2[-7])

print("#" * 50)
print("t index:", str1.index("t"))

############################String Formating##################################
# 1. using + operator
name = "Swital Macwan"
experience = 8
domain = "Automation Testing"
# I am Swital Macwan, 8 years in Automation Testing Field
##### String concatination ["sentence" +variable+ "sentence" +variable+]
resultcon = "I am " + name + " , " + str(experience) + " years in " + domain + " Field"
print("Result is:", resultcon)

# 2. using string format ["sentence {} sentence".formate(variable, variable)]
resultformat = "I am {} , {} years in {} Field".format(name, experience, domain)
print("Result is:", resultformat)

# 3. using f string format [f"sentence {string variable} sentence"]
resultformat1 = f"I am {name} , {experience} years in {domain} Field"
print("Result is:", resultformat1)

##################### convert string into raw string ########################
# \t : add space in string
# \n :  add next line in string.
print("#" * 50)
str_b = "Hello \t\t we are \n Learning Python"
str_br = r"Hello \t\t we are \n Learning Python"
print(str_b)
print("#" * 50)
print(str_br)

############################ Slicing ######################################
# Rule1 : str[start index:  end index]
"""
->  In this rule it will always get output from left to right.
->  default start index value is 0
->  default end index value is end of string.
->  start index and end index could be positive negative.
->  Output will include the start index value and exclude end index value
"""
# This will only go right to left no matter what index is "----->", means no reverse string
str_s = "The Python Automation"
#        "0123456789....."
#        "-9-8-7-6-5-4-3-2-1"
print("Positive index:", str_s[1:11])
print("#" * 50)
print("Negative index:", str_s[-12: -1])
print("#" * 50)
print("Positive  default start index:", str_s[:5])
print("#" * 50)
print("Positive  default end index:", str_s[3:])
print("#" * 50)
print("negative start index:", str_s[-3:])
print("#" * 50)
print("negative start index:", str_s[:-5])

# Rule2 : str[start index:  end index: step value]
"""
-> In this rule, output will include start index value and exclude end index value
-> default start index is zero (0) if step value is +ve
-> default start index is -1 if step value is -ve
-> default end index will be end of string if step value is +ve
-> default end index will be start of string if step value is -ve
"""
print("#" * 50)
str_s1 = "Python slicing program"
print("Positive index: ", str_s1[0:6:1])
print("#" * 50)
print("Positive index without start index: ", str_s1[:6:1])
print("#" * 50)
print("Positive index without end index: ", str_s1[4::1])
print("#" * 50)
print("Positive index without start and end index: ", str_s1[::1])
print("#" * 50)
print("Negative index : ", str_s1[-3:-7:-1])
print("#" * 50)
print("Negative index : ", str_s1[-9:-1:1])
print("#" * 50)
print("Negative index without start index: ", str_s1[:-6:-1])
print("#" * 50)
print("Negative index without start index but positive step value: ", str_s1[:-6:1])
print("#" * 50)
print("Negative index without end index: ", str_s1[-4::-1])
print("#" * 50)
print("Negative index without end index but positive step value:: ", str_s1[-4::1])
print("#" * 50)
print("Negative index without start and end index: ", str_s1[::-1])

# Homework slicing
str3 = "Virat is Best Batsman of India"
# output1 = "VViratt iiss BBestt BBatsmann ooff IIndiaa"
# output2 = "airat is Best Batsman of IndiV"
# output3 = "tiraV si tesB natsmaB fo andiI"
str3_1 = "Virat"
str3_2 = "is"
str3_3 = "Best"
str3_4 = "Batsman"
str3_5 = "of"
str3_6 = "India"
result_output1 = [str3_1[0]+str3_1+str3_1[4] + " " +
                  str3_2[0]+str3_2+str3_2[1] + " " +
                  str3_3[0]+str3_3+str3_3[3] + " " +
                  str3_4[0]+str3_4+str3_4[6] + " " +
                  str3_5[0]+str3_5+str3_5[1] + " " +
                  str3_6[0]+str3_6+str3_6[4]]
print(result_output1)

result_output2 = ["a"+str3_1[1:] + " " +
                  str3_2 + " " +
                  str3_3 + " " +
                  str3_4 + " " +
                  str3_5 + " " +
                  str3_6[:4]+"V"]
print(result_output2)

result_output3 = ["t"+str3_1[1:4]+"V" + " " +
                  "s"+ str3_2[0:0] + "i" + " " +
                  "t" + str3_3[1:3] + "B" + " " +
                  "n"+ str3_4[1:6] + "B" + " " +
                  "f" + str3_5[0:0] + "o" + " " +
                  "a" + str3_6[1:4]+"I"]
print(result_output3)

str3 = "Virat is Best Batsman of India"

result = ""

for ch in str3:
    result = result + ch*2   # repeat each character twice

print(result)

str3 = "Virat is Best Batsman of India"

words = str3.split()   # split into words
result = []

for word in words:
    if len(word) > 1:
        new_word = word[0]*2 + word[1:-1] + word[-1]*2
    else:
        new_word = word * 2   # for single letter words

    result.append(new_word)

final_output = " ".join(result)

print(final_output)

s = "tiraV si tesB natsmaB fo andiI"

result = " ".join(
    word[-1] + word[1:-1] + word[0]
    for word in s.split()
)

print(result)
