str="hello we learnig python"
output={}

wordlist =str.split()
for word in wordlist:
    fchar=word[0]
    output[fchar]=word

print(output)

str1= "we are learning python"
output={}
wordlist= str1.split()
for word in  wordlist:
    fchar= word[0]+word[-1]
    output[fchar]=word
print(output)


