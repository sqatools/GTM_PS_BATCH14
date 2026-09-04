convert string to raw string
#\t give the space to string
#\n new line
#r used infront of string cancel the special charcter
str_v= r"hello \t\t we are learning \n python"
# print(str_v)

#############slicing#########
str_d="python programming"
# print(str_d[0:6])
# print(str_d[0:5:1])
print(str_d[-7:0:-1])
print(str_d[-1:-len(str_d)-1:-1])
#print all the charcter 1 and last charcter
print (str_d[1:-1])

str3="virat is best batsman in India"
#"vvirat iis bbest bbatsman iin IIndia"
#"airat is best batsman in Indiv"
#"tirav si tesb natsmab ni andii"


#how to apply loop in the string without indexing

for char in str3:
    print(char)

#how to apply loop in the string with indexing
for char in range(len(str3)):
    print(char,str3[char])
##enumerate
print("enumerate")
for i,char in enumerate(str3):
    print(char)

print("*"*80)
#"vvirat iis bbest bbatsman iin IIndia"
v="virat is best batsman in India"
print("v" "virat " "i" "is " "b" "best " "b" "batsman " "i" "in " "I" "India")

print("*"*80)
#second homework-#"airat is best batsman in Indiv"
v="virat is best batsman in India"
result = v.replace("virat", "airat").replace("India", "Indiv")
print(result)


print("*"*50)
##"tirav si tesb natsmab ni aidni"
v="virat is best batsman in India"
# print(v[-1:-30:-1], end="")
word=v.(reversed)
print(word)







