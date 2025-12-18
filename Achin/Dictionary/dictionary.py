str="Hello we Are Learning Python"

wordlist=str.split()
output={}
for word in wordlist:
    f_word=word[0]
    l_word=word[-1]
    merge_word=f_word+l_word
    output[merge_word]=word

print(output)

#to print square of all values
output={'a': 5, 'b':3, 'c': 6, 'd' : 8}

for key, value in output.items():
    print(key, value**2)

#to copy one dict data to another
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}

dict2=dict1.copy()
dict1.clear()

print(dict1)
print(dict2)

#concatenate 2 dictionaries
dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary': '$25k'}

dict1.update(dict2)
print(dict1)

#Python Dictionary program to get a list of odd and even keys from the dictionary

Input={1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
even=[]
odd=[]
for key, value in Input.items():
    if key %2==0:
      even.append([key, value])
    else:
      odd.append([key, value])

print(even)
print(odd)

#Python Dictionary Program to create a dictionary from two lists.
list1 = ['a','b','c','d','e']
list2 = [12,23,24,25,15,16]
dict1 = {}

result = dict(zip(list1, list2))
print("result :", result)

#Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.

list1 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {}

# iterate through the list of values
for val in list1:
    # val is divisible by 2, then value is even number
    if val % 2 == 0:
        # dict store value as square
        dict1[val] = val**2
    else:
        # dict store value as cube
        dict1[val] = val**3

print("result dictionary:", dict1)

#print unique values from dictionary
input={'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
duplicatedict={}

for key, value in input.items():
    if value not in duplicatedict.values():
        duplicatedict[key]=value
    else:
        continue
print(duplicatedict)