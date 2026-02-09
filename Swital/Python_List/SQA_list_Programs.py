# 1). Python program to calculate the square of each number from the given list.
l1 = [1,3,4,5,8]
for a in l1:
    print("Square of", a, ":", a**2)

# 2). Python program to combine two lists.
l2 = [2,3,5,6,1]
l2p = [7,8,9]
print("Combine two list:", l2+l2p)

# 3). Python program to calculate the sum of all elements from a list.
l3 = [3,6,2,8,7]
print("Summation is:", sum(l3))

# 4). Python program to find a product of all elements from a given list.
l4 = [1,4,2,3,5]
var = 1
for val in l4:
    var *= val
print("Product of all elements:", var)

# 5). Python program to find the minimum and maximum elements from the list.
l5 = [3,2,5,3,6]
print("Maximum number is:", max(l5))
print("Minimum number is:", min(l5))

# 6). Python program to differentiate even and odd elements from the given list.
l6 = [3,4,2,5,6,8]
odd = []
even = []
for val in l6:
    if val%2 == 0:
        even.append(val)
    else:
        odd.append(val)
print("Even numbers list:", even)
print("Odd numbers list:", odd)

# 7). Python program to remove all duplicate elements from the list.
l7 = [3,2,4,5,2,5,3,2,6,7,1]
list1 = []
for val in l7:
    if val not in list1:
        list1.append(val)
print(list1)

# 8). Python program to print a combination of 2 elements from the list whose sum is 10.
l8 = [4,7,5,3,5,2,8,5]
total = []
for i in range(len(l8)):
    for j in range(i+1, len(l8)):
        if l8[i]+l8[j] == 10 and (l8[i], l8[j]) not in total and (l8[j], l8[i]) not in total:
            total.append((l8[i], l8[j]))
            
print(total)

l8 = [4,7,5,3,5,2,8,5]
seen = set()
pairs = []

for num in l8:
    diff = 10 - num
    if diff in seen:
        pairs.append((diff, num))
    seen.add(num)

print(pairs)

# 9). Python program to print squares of all even numbers in a list.
l9 = [4,5,2,7,6,9]
for val in l9:
    if val%2 == 0:
        print(f"{val} is even and its square is:", val**2)

# 10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
#Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
#Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]

l10 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
even = []
odd = []
for val in l10:
    if val %2 == 0:
        even.append(val)
    else:
        odd.append(val)
odd.extend(even)
print(odd)

# 11).  Python program to get common elements from two lists.
"""Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
Outputt : [4, 5, 7, 2] """

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
list3 = []
for val in list1:
    if val in list2:
        list3.append(val)
print(list3)

# 12). Python program to reverse a list with for loop.
list1 = [4, 5, 7, 9, 2, 1]
for i in range(len(list1)-1,-1,-1):
    print(list1[i], end= " ")

print("\n##########")

# 13). Python program to reverse a list with a while loop.
list1 = [4, 5, 7, 9, 2, 1]
count = len(list1) - 1
while count >= 0:
    print(list1[count], end=" ")
    count -= 1

print("\n##########")

# 14). Python program to reverse a list using index slicing.
list1 = [4, 5, 7, 9, 2, 1]
print("Using index slicing:", list1[::-1])

# 15). Python program to reverse a list with reversed and reverse methods.
list1 = [4, 5, 7, 9, 2, 1]
list1.reverse()
print("Using reverse:", list1)

list1 = [4, 5, 7, 9, 2, 1]
print("Using reversed:", list(reversed(list1)))

# 16). Python program to copy or clone one list to another list.
l16 = [3,5,2,9,1]
lop = []
for val in l16:
    lop.append(val)
print("Without copy method:", lop)

op = l16.copy()
print("With copy method:", op)

# 17). Python program to return True if two lists have any common member.
l17 = [2,1,6,4,5]
l17_1 = [5,4,6,7,2]
common_list = []
for val in l17:
    if val in l17_1:
        common_list.append(val)
if len(common_list)>0:
    print("True")
else:
    print("False")

# 18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
l18 = [2,4,3,6,5,9,8]
out = []

#for i in range(len(l18)):
#    if i not in[1,3,6]:
#        out.append(l18[i])
#print(out)

for i, val in enumerate(l18):
    if i not in(1,3,6):
        out.append(l18[i])
print(out)

# 19). Python program to remove negative values from the list.
l19 = [-4,-5,1,6,7,-2]
result = []
for val in l19:
    if val>0:
        result.append(val)
print(result)

# 20). Python program to get a list of all elements which are divided by 3 and 7.
l20 = [3,21,6,63,7,49]
result1 = []
for val in l20:
    if val%3==0 and val%7==0:
        result1.append(val)
print(result1)

# 21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).
def palindrom_reversem():
    l21 = [2,3,4,3,2,3,2]
    result = l21.reverse()
    if l21 == result:
        print("Palindrome list")
    else:
        print("Not Palindrome list")
#palindrom_reversem()
####################################################
def palindrom_ind():
    l21 = [2,3,4,3,2]
    result = l21[::-1]
    if l21 == result:
        print("Palindrome list")
    else:
        print("Not Palindrome list")
# palindrom_ind()
#####################################################
def palindrom_revd():
    l21 = [2,3,4,3,2]
    result = list(reversed(l21))
    if l21 == result:
        print("Palindrome list")
    else:
        print("Not Palindrome list")
# palindrom_revd()
#####################################################
def palindrom_loop():
    l21 = [2,3,4,3,2]
    result = []
    for i in range(len(l21)-1, -1, -1):
        result.append(l21[i])
    if l21 == result:
        print("Palindrome list")
    else:
        print("Not Palindrome list")
palindrom_loop()

# 22). Python Program to get a list of words which has vowels in the given string.
#Input: “www Student ppp are qqqq learning Python vvv”
#Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]
input_str = "www Student ppp are qqqq learning Python vvv"
word_list = input_str.split(" ")
vowels = "aeiou"
result = []
for word in word_list:
    for char in word:
        if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
            result.append(word)
            break
print(result)

#23). Python program to add 2 lists with extend method.
l23 = [2,4,3,5,7]
l23_1 = [1,2,8]
l23.extend(l23_1)
print(l23)

# 24). Python program to sort list data, with the sort and sorted method.
l24 = [5,2,4,7,1]
l24.sort()
print("with the sort:", l24)

result = sorted(l24)
print("with the sorted:", result)

# 25). Python program to remove data from the list from a specific index using the pop method.
l25 = [2,4,6,1,7]
l25.pop(3)
print("After pop from 3rd index:",l25)


# 26). Python program to get the max, min, and sum of the list using in-built functions.
l26 = [2,5,3,7,8]
print("Max number:", max(l26))
print("Min number:", min(l26))
print("Sum of number:", sum(l26))

# 27). Python program to check whether a list contains a sublist.
l27 = [2,5,3,7,8]
l27_1 = [2,7,3,8,5]
count = 0
for element in l27:
    for val in l27:
        if val == element:
            count +=1
if count == len(l27_1):
    print("The list contains sublist ")
else:
    print("The list does not contains sublist ")
# 28). Python program to generate all sublists with 5 or more elements in it from the given list.
#Importing combinations - NOT UNDERSTAND
from itertools import combinations

#Input list
list1 = [1,3,5,8,0,22,45]

#Creating an empty list
sub = []

for i in range(0,len(list1)+1):
#Checking for combinations
    for sublist in combinations(list1,i):
        temp = list(sublist)
        if len(temp) > 4:
            sub.append(temp)

#Printing output
print(sub)

# 29). Python program to find the second largest number from the list.
l29 = [3,5,7,9,1]
r2 = sorted(l29)
print("second largest number:", r2[-2])

# 30). Python program to find the second smallest number from the list.
l30 = [3,5,7,9,1]
r2 = sorted(l30)
print("second smallest number:", r2[1])

# 31). Python program to merge all elements of the list in a single entity using a special character.
l31 = ['a','b','c','d','e','f','g']
print("Element to combine using special character:", "$".join(l31))

# 32). Python program to get the difference between two lists.
l32 = [3,5,7,8,2]
l32_1 = [5,7,8,9,4]
list_result = []
for val in l32:
    if val not in l32_1:
        list_result.append(val)
for val in l32_1:
    if val not in l32:
        list_result.append(val)
print(list_result)

# 33). Python program to reverse each element of the list.
#Input = [‘Sqa’, ‘Tools’, ‘Online’, ‘Learning’, ‘Platform’]
#output = [‘aqS’, ‘slooT’, ‘enilno’, ‘gninraeL’, ‘mroftalP’]
input = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
output = []
for val in input:
    output.append(val[-1:]+ val[1:-1]+val[:1])
print(output)

#34). Python program to combine two list elements as a sublist in a list.
#list1 = [3, 5, 7, 8, 9]
#list2 = [1, 4, 3, 6, 2]
#Output = [[3, 1], [5, 4], [7, 3], [8, 6], [9, 2]]

list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
result = []
for (a,b) in zip(list1,list2):
    result.append(list((a,b)))
print(result)

# 35). Python program to get keys and values from the list of dictionaries.
#Input : [{‘a’:12}, {‘b’: 34}, {‘c’: 23}, {‘d’: 11}, {‘e’: 15}]
#Output :  [‘a’, ‘b’, ‘c’, ‘d’, ‘c’]
#                [12, 34, 23, 11, 15]

input = [{'a':12}, {'b': 34}, {'c': 23}, {'d': 11}, {'e': 15}]
key = []
value = []
for element in input:
    for val in element:
        key.append(val)
        value.append(element[val])
print(key,value)

        
