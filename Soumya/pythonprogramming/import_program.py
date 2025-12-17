# reverse a string without using reverse method
s1="testtest"
print(s1[::-1])

#Check Palindrome
print("*"*50)
s1="madam"
if s1==s1[::-1]:
    print("given string is palindrome")
else:
    print("given string is not palindrome")

#Count Occurrence of Each Character
print("*"*50)
s2="automation"
d={}
for ch in s2:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
print(d)

#Find Duplicate Characters in String
s3="testtest"
dup=[]
for ch in s3:
    if s3.count(ch)>1 and ch not in dup:
        dup.append(ch)
print(dup)

#Find Largest Number in List (Without max)
l1=[1, 6, 87, 81, 89]
largest=l1[0]
