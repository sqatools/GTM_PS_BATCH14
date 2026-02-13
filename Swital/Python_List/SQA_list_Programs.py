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
list1 = [1,3,5,8,0,22,45]

sub = []

for i in range(5, len(list1)+1):   # start from 5 directly
    for c in combinations(list1, i):
        sub.append(list(c))

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

# 36). Python program to get all the unique numbers in the list.
l36 = [3,5,3,6,1,2,5]
result = list(set(l36))
print(result)

#############################################3
result1 = []
for val in l36:
    if val not in result1:
        result1.append(val)
print(result1)

# 37). Python program to convert a string into a list.
l37 = "Flooring"
list_data = []
for ch in l37:
    list_data.append(ch)
print("convert a string into a list:", list_data)

# 38). Python program to replace the last and the first number of the list with the word.
#Input: [12, 32, 33, 5, 4, 7]
#output : [‘SQA’, 32, 33, 5, 4, ‘Tools’]
input =  [12, 32, 33, 5, 4, 7]
input[0] = "SQA"
input[-1] = "Tools"
print(input)

#39). Python program to check whether the given element is exist in the list or not.
l39 = [3,4,5,6,7]
print("value exist:", 6 in l39)

# 40). Python program to remove all odd index elements.
#Input: [12, 32, 33, 5, 4, 7, 33]
#Output: [12,33,4,33]
input = [12, 32, 33, 5, 4, 7, 33]
output = []
for i in range(len(input)):
    if i%2 == 0:
        output.append(input[i])
print(output)

# 41). Python program to take two lists and return true if then at least one common member.
list1 = [2,3,4,5,6]
list2 = [3,4,5,7,8]
count = 0
for val in list1:
    if val in list2:
        count +=1
if count>0:
    print("True")
else:
    print("False")

#42). Python program to convert multiple numbers from a list into a single number.
#Input: [12, 45, 56]
#Output:124556
list42 = [12, 45, 56]
for val in list42:
    print(val, end="")
############################33
print()

# 43). Python program to convert words of a list into a single string.
#Input: [‘Sqa’, ‘Tools’, ‘Best’, ‘Learning’, ‘Platform’]
#Output: SqaToolsBestLearningPlatform
# same as above but if dont want to change original variable then use below
l43 = ['Sqa', 'Tools', 'Best', 'Learning', 'Platform']
output =''
for val in l43:
    if val not in output:
        output = output + val
print(output, end="")
print()
# 44). Python program to print elements of the list separately.
"""Input: [(‘Black’, ‘Yellow’, ‘Blue’), (50, 55, 60), (30.0, 50.5, 55.66)]
Output:
(‘Black’, ‘Yellow’, ‘Blue’)
(50, 55, 60)
(30.0, 50.5, 55.66)"""
input = [('Black', 'Yellow', 'Blue'), (50, 55, 60), (30.0, 50.5, 55.66)]
for val in input:
    print(val)

#45). Python program to create a sublist of numbers and their squares from 1 to 10.
#Output : [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]
output = [[i, i**2] for i in range(1,11)]
print(output)

# 46). Python program to create a list of five consecutive numbers in the list.
#Output : [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
list1 = [[5*i + j for j in range(1,6)] for i in range(4)]
print(list1)

# 47). Python program to insert a given string at the beginning of all items in a list.
#Input: [1, 2, 3, 4, 5], Sqa
#Output: [‘Sqa1’, ‘Sqa2’, ‘Sqa3’, ‘Sqa4’, ‘Sqa5’]
l47 = [1, 2, 3, 4, 5], 'Sqa'
print([f"Sqa{val}" for val in l47[0]])

# 48). Python program to iterate over two lists simultaneously and create a list of sublists.
#list1 = [1, 3, 5, 7, 9]
#list2 = [8, 6, 4, 2, 10]
#output = [[1, 8], [3, 6], [5, 4], [7, 2], [9, 10]]

list1 = [1, 3, 5, 7, 9]
list2 = [8, 6, 4, 2, 10]
output = []
for (a,b) in zip(list1,list2):
    data = [a,b]
    output.append(data)
print(output)

# 49). Python program to move all positive numbers on the left side and negative numbers on the right side.
#Input: [2, -4, 6, 44, -7, 8, -1, -10]
#Output: [2, 6, 44, 8, -4, -7, -1, -10]
l49 = [2, -4, 6, 44, -7, 8, -1, -10]
var = 0
for i in range(0,len(l49)):
    if l49[i] > 0:
        temp = l49[i]
        l49[i] = l49[var]
        l49[var] = temp
        var += 1
print(l49)

################################
l49 = [2, -4, 6, 44, -7, 8, -1, -10]
positive = []
negative = []
for val in l49:
    if val>0:
        positive.append(val)
    else:
        negative.append(val)
print(positive+negative)

# 50). Python program to move all zero digits to the end of a given list of numbers.
#Input: [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
#Output: [3, 4, 6, 4, 22, 3, 21, 0, 0, 0, 0, 0, 0, 0, 0]
l50 = [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
positive = []
zero = []
for val in l50:
    if val>0:
        positive.append(val)
    else:
        zero.append(val)
print(positive+zero)

#51). Python program to find the list in a list of lists whose sum of elements is the highest.
#Input: [[11, 2, 3], [4, 15, 6], [10, 11, 12], [7 8, 19]]
#Output: [7, 8, 19]
l51 = [[11, 2, 3], [4, 15, 6], [10, 11, 12], [7, 8, 19]]
print(max(l51, key = sum))

# 52). Python program to find the items that start with a specific character from a given list.
"""Input: [‘abbcd’, ‘ppq, ‘abdd’, ‘agr’, ‘bhr’, ‘sqqa’, tools, ‘bgr’]
 
# item starts with a from the given list.
[‘abbcd’, ‘abdd’, ‘agr’]
 
# item starts with b from the given list.
[‘bhr’, ‘bgr’]
 
# item starts with c from the given list.
[]"""
l52 = ['Abbcd', 'ppq', 'abdd', 'agr', 'bhr', 'sqqa', 'tools', 'bgr']
a_list = []
b_list = []
c_list = []
for val in l52:
    if val.lower().startswith("a"):
        a_list.append(val)
    elif val.startswith("b"):
        b_list.append(val)
    elif val.startswith("c"):
        c_list.append(val)
print(a_list)
print(b_list)
print(c_list)

######################################
words = ["abbcd", "ppq", "abd", "agr", "bhr", "sqqa", "tools", "bgr"]

result = {"a": [], "b": [], "c": []}

for word in words:
    first = word[0].lower()
    if first in result:
        result[first].append(word)

print(result["a"])
print(result["b"])
print(result["c"])

# 53). Python program to count empty dictionaries from the given list.
#Input: [{}, {‘a’: ‘sqatools’}, [], {}, {‘a’: 123}, {},{},()]
#empty_count: 3
l53 = [{}, {'a': 'sqatools'}, [], {}, {'a': 123}, {},{},()]
output = []
for element in l53:
    if isinstance(element, dict):
        if len(element) == 0:
            output.append(element)
print(len(output))

# 54). Python program to remove consecutive duplicates of given lists.
#Input: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
#Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 4]
l54 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
output = []
for val in l54:
    if val not in output:
        output.append(val)
print(output)

#####################33
#Input list
list1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

#Creating empty list
list2 = []

from itertools import groupby
for value in groupby(list1):
    list2.append(value[0])

#Printing output
print(list2)

# 55). Python program to pack consecutive duplicates of given list elements into sublists.
#Input: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
#Output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6], [7], [8, 8], [9]]
l55 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
from itertools import groupby
output = [list(data) for key, data in groupby(l55)]
print(output)

# 56). Python program to split a given list into two parts where the length of the first part of the list is given.
#Input: [4, 6, 7, 3, 2, 5, 6, 7, 6, 4]
#length of the first part is 4
#Output: [[4, 6, 7, 3], [2, 5, 6, 7, 6, 4]]
l56 = [4, 6, 7, 3, 2, 5, 6, 7, 6, 4]
output = []
output.append(l56[:4])
output.append(l56[4:])
print(output)

# 57). Python program to insert items at a specific position in the list.
"""Input: [2, 4, 6, 8, 3, 22]
Index: 3
Item: 55
Output: [2, 4, 6, 55, 8, 3, 22]"""
l57 = [2, 4, 6, 8, 3, 22]
l57.insert(3,55)
print(l57)

# 58). Python program to select random numbers from the list.
#Input: [1, 4, 5, 7, 3, 2, 9]
#Selected 4 random numbers from the list.
import random

l58 = [1, 4, 5, 7, 3, 2, 9]
count = 0
list1 = []
while count<4:
    list1.append(random.choice(l58))
    count += 1
print(list1)



#59). Python program to create a 3*3 grid with numbers.
#Output: [[4, 5, 6], [4, 5, 6], [4, 5, 6]]
output = []
for i in range(3):
    output.append([])
    for j in range(4,7):
        output[i].append(j)
print(output)

#60). Python program to zip two lists of lists into a list.
#list1: [[1, 3], [5, 7], [9, 11]]
#list2: [[2, 4], [6, 8], [10, 12, 14]]
list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]
print(list(zip(list1, list2)))

# 61). Python program to convert the first and last letter of each item from Upper case and lowercase.
#Input: [‘Learn’, ‘python’, ‘From’, ‘Sqa’, tools]
#Output =
#[‘LearN ‘, ‘PythoN ‘, ‘FroM ‘, ‘SqA ‘, ‘ToolS ‘]
#[‘learn ‘, ‘python ‘, ‘from ‘, ‘sqa ‘, ‘tools ‘]

l61 = ['Learn', 'python', 'From', 'Sqa', 'tools']
output =[]
output1 =[]
for val in l61:
    output.append(val[0].lower()+val[1:-1]+val[-1].upper())

for val in l61:
    output1.append(val[0].lower()+val[1:-1]+val[-1].lower())
print(output)
print(output1)

# 62). Python to find maximum and minimum values in the given heterogeneous list.
#Input: [‘Sqa’, 6, 5, 2, ‘Tools’]
#Output: [6,2]
l62 = ['Sqa', 6, 5, 2, 'Tools']
Max = max(value for value in l62 if isinstance(value, int))
Min = min(value for value in l62 if isinstance(value, int))

print(Max, Min)

# 63). Python program to sort a given list in ascending order according to the sum of its sublist.
#Input: [[3, 5, 6], [2, 1, 3], [5, 1, 1], [1, 2, 1], [0, 4, 1]]
#            14         6         7           4          5
#Output = [[1, 2, 1], [0, 4, 1], [2, 1, 3], [5, 1, 1], [3, 5, 6]]
list1 = [[3, 5, 6], [2, 1, 3], [5, 1, 1], [1, 2, 1], [0, 4, 1]]
print(sorted(list1, key = sum))

# 64). Python program to extract the specified sizes of strings from a given list of string values.
#Input: [‘Python’, ‘Sqatools’, ‘Practice’, ‘Program’, ‘test’, ‘list’]
##size = 8
#Output: [‘Sqatools’, ‘Practice’]

l64 = ['Python', 'Sqatools', 'Practice', 'Program', 'test', 'list']
output = []
for val in l64:
    if len(val)>=8:
        output.append(val)
print(output)

#65). Python program to find the difference between consecutive numbers in a given list.
#Input list: [1, 1, 3, 4, 4, 5, 6, 7]
#Output list: [0, 2, 1, 0, 1, 1, 1]
l65 = [1, 1, 3, 4, 4, 5, 6, 7]
output = []
for a,b in zip(l65[:-1], l65[1:]):
    difft = b-a
    output.append(difft)
print(output)

# 66). Python program to calculate the average of the given list.
#Input : [3, 5, 7, 2, 6, 12, 3]
#Output: 5.428571428571429
l66 = [3, 5, 7, 2, 6, 12, 3]
output = sum(l66)/len(l66)
print(output)

# 67). Python program to count integers in a given mixed list.
#Input list: [‘Hello’, 45, ‘sqa’,  23, 5, ‘Tools’, 20]
#Output: 4
l67 = ['Hello', 45, 'sqa',  23, 5, 'Tools', 20]
count = 0
for value in l67:
    if isinstance(value, int):
        count += 1
print(count)