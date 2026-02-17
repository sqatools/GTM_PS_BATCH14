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

# 68). Python program to access multiple elements of the specified index from a given list.
#Input list: [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
#Index list: [0, 3, 5, 6]
#Output: [2, 7, 1, 5]
l68 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
index_val = [0, 3, 5, 6]
output = []
for value in index_val:
    output.append(l68[value])
print(output)

# 69). Python program to check whether a specified list is sorted or not.
"""Input list : [1, 2, 3, 5, 7, 8, 9]
Output: True
 
Input list: [3, 5, 1, 6, 8, 2, 4]
Output: False"""
l69 = [1, 2, 3, 5, 7, 8, 9]
output = sorted(l69)
if l69 == output:
    print("True")
else:
    print("False")

l69_1 = [3, 5, 1, 6, 8, 2, 4]
output1 = sorted(l69_1)
if l69_1 == output1:
    print("True")
else:
    print("False")

#70). Python program to remove duplicate dictionaries from a given list.
#Input : [{‘name’: ‘john’}, {‘city’: ‘mumbai’}, {‘Python’: ‘laguage’}, {‘name’: ‘john’}]
#Output: [{‘city’: ‘mumbai’}, {‘Python’: ‘laguage’}]
l70 = [{'name': 'john'}, {'city': 'mumbai'}, {'Python': 'language'}, {'name': 'john'}]
output = []
for value in l70:
    if value not in output:
        output.append(value)
print(output)

#71). Python program to check if the elements of a given list are unique or not.
input =  [2, 5, 6, 7, 4, 11, 2, 4, 66, 21, 22, 3]
output = []
for val in input:
    if val not in output:
        output.append(val)
print(output)

# 72). Python program to remove duplicate sublists from the list.
#Input: [[1, 2], [3, 5], [1, 2], [6, 7]]
#Output: [[3, 5],[6, 7]]
l72 = [[1, 2], [3, 5], [1, 2], [6, 7]]
output = []
for val in l72:
    if val not in output:
        output.append(val)
print(output)

# 73). Python program to create a list by taking an alternate item from the list.
#Input: [3, 5, 7, 8, 2, 9, 3, 5, 11]
#Output: [3, 7, 2, 3, 11]
l73= [3, 5, 7, 8, 2, 9, 3, 5, 11]
output = l73[:len(l73):2]
print(output)

# 74). Python program to remove duplicate tuples from the list.
#Input: [(2, 3), (4, 6), (5, 1), (2, 3), (7, 9), (5, 1)]
#Output: [(2,3), (4, 6), (5,1), (7, 9)]

l74 = [(2, 3), (4, 6), (5, 1), (2, 3), (7, 9), (5, 1)]
output = []
for val in l74:
    if val not in output:
        output.append(val)
print(output)

# 75). Python program to insert an element before each element of a list.
#Input :[3, 5, 7, 8]
#element = ‘a’
#Output: [‘a’, 3, ‘a’, 5, ‘a’, 7, ‘a’, 8]
l75 = [3, 5, 7, 8]
output = []
for value in l75:
    for a in ('a', value):
        output.append(a)
print(output)

#76). Python program to remove the duplicate string from the list.
#Input: [‘python’, ‘is’, ‘a’, ‘best’, ‘language’, ‘python’, ‘best’]
#Output: [‘python’, ‘is’, ‘a’, ‘best’, ‘language’]
l76 = ['python', 'is', 'a', 'best', 'language', 'python', 'best']
output = []
for val in l76:
    if val not in output:
        output.append(val)
print(output)

# 77). Python program to get the factorial of each item in the list.
l77 = [3,5,7]
output = []
for val in l77:
   fact = 1
   for i in range(1, val+1):
       fact *= i
   output.append(fact)
print(output)

#78). Python program to get a list of Fibonacci numbers from 1 to 20.
num1 = 0
num2 = 1
list1 = []
for i in range(1,21):
    list1.append(num1)
    n2 = num1 + num2
    num1 = num2
    num2 = n2

print(list1)

# 79). Python program to reverse all the numbers in a given list.
#Input : [123, 145, 633, 654, 254]
#Output: [321, 541, 336, 456, 452]
l79 = [123, 145, 633, 654, 254]
output = []

for val in l79:
    reverse = 0
    while val != 0:
        digit = val%10
        reverse = reverse*10 +digit
        val //= 10
    output.append(reverse)
print(output)

# 80). Python program to get palindrome numbers from a given list.
#Input : [121, 134, 354, 383, 892, 232]
#Output : [121, 282, 232]
l80 = [121, 134, 354, 383, 892, 232]
output = []
for val in l80:
    if str(val) == str(val)[::-1]:
        print("Palindrome")
        output.append(val)
    else:
        print("Not palindrome")

print(output)

# 81). Python program to get a count of vowels in the given list.
#Input : [‘Learning’, ‘Python’, ‘From’, ‘SqaTool’]
#Output : 8
l81 = ['Learning', 'Python', 'From', 'SqaTool']
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for word in l81:
    for ch in word:
        if ch in vowels:
            count += 1
print(count)

# 82). Python program to get the list of prime numbers in a given list.
#Input : [11, 8, 7, 19, 6, 29]
#Output : [11,  7,  19, 29]
l82 = [11, 8, 7, 19, 6, 29]
output = []
for num in l82:
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            output.append(num)
print(output)

# 83). Python program to get a list with n elements removed from the left and right.
#Input : [2, 5, 7, 9, 3, 4]
#Remove 1 element from left
#[5, 7, 9, 3, 4]

l83 = [2, 5, 7, 9, 3, 4]
result = l83[1:]
print("Remove 1 element from left", result)
##########################################################
l83 = [2, 5, 7, 9, 3, 4]
result = l83[:-1]
print("Remove 1 element from the right", result)
##############################################################
l83 = [2, 5, 7, 9, 3, 4]
result = l83[2:]
print("Remove 2 elements from left", result)
##################################################################
l83 = [2, 5, 7, 9, 3, 4]
result = l83[:-2]
print("Remove 2 elements from right", result)

# 84). Python program to create a dictionary with two lists.
"""Input :
list1 : [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]
list2 : [234, 123, 456, 343, 223]
Output: {‘a’: 234, ‘b’: 123, ‘c’: 456, ‘d’: 343, ‘e’: 223}"""
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [234, 123, 456, 343, 223]
output = dict(zip(list1, list2))
print(output)

output = {}

for i in range(len(list1)):
    output[list1[i]] = list2[i]
print(output)

# 85). Python program to remove the duplicate item from the list using set.
#Input : [2, 5, 7, 8, 2, 3, 4, 12, 5, 6]
#Output : [2, 5, 7, 8, 3, 4, 12, 6]
l85 = [2, 5, 7, 8, 2, 3, 4, 12, 5, 6]
output = list(set(l85))
print(output)

# 86). Python program to insert a sublist into the list at a specific index.
"""Input : [4, 6, 8, 2, 3, 5]
sublist, index
[5, 2, 6], 3
Output: [4, 6, 8, [5, 2, 6], 2, 3, 5]"""
l86 = [4, 6, 8, 2, 3, 5]
l86.insert(3, [5, 2, 6])
print(l86)

# 87). Python program to calculate the bill per fruit purchased from a given fruits list.
"""Input =
Fruit list with Price: [[‘apple’, 30], [‘mango’, 50], [‘banana’, 20], [‘lichi’, 50]]
Fruit with quantity: [[‘apple’, 2]]
Output =
Fruit: Apple
Bill: 60
Fruit: mango
Bill: 500"""
Fruit_list_with_Price = [['apple', 30], ['mango', 50], ['banana', 20], ['lichi', 50]]
Fruit_Price = dict(Fruit_list_with_Price )
Fruit_with_quantity = [['apple', 2]]
Fruit_quantity = dict(Fruit_with_quantity)
total = 0
for fruit, qty in Fruit_quantity.items():
    total += Fruit_Price[fruit]*qty
print(total)

#####################################################
for a in Fruit_list_with_Price:
    for b in Fruit_with_quantity:
        if a[0] == b[0]:
            print(a[0])
            print(a[1]*b[1])

# 88). Python program to calculate percentage from a given mark list, the max mark for each item is 100.
#Marks_list : [80, 50, 70, 90, 95]
#Output: 77%
marks_list = [80, 50, 70, 90, 95]
total = sum(marks_list)//len(marks_list)
print(total,"%")

#89). Python program to get the list of all palindrome strings from the given list.
#Input: [‘data’, ‘python’, ‘oko’, ‘test’, ‘ete’]
#Output: [‘oko’, ‘ete’]

l89 = ['data', 'python', 'oko', 'test', 'ete']
output = []
for val in l89:
    if str(val) == str(val)[::-1]:
        output.append(val)
print(output)

# 90). Python program to flatten a given nested list structure.
#Input: [0, 12, [22, 32], 42, 52, [62, 72, 82], [92, 102, 112, 122]]
#Output: [0, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122]
l90 = [0, 12, [22, 32], 42, 52, [62, 72, 82], [92, 102, 112, 122]]
result = []

for val in l90:
    if isinstance(val, list):
        for var in val:
            result.append(var)
    else:
        result.append(val)

print(result)

# 91). Python program to convert tuples in the list into a sublist.
#Input: [(3, 5), (6, 8), (8, 11), (12, 14), (17, 23)]
#Output: [[3, 5], [6, 8], [8, 11], [12, 14], [17, 23]]
l91 = [(3, 5), (6, 8), (8, 11), (12, 14), (17, 23)]
result = []
for val in l91:
    if isinstance(val, tuple):
        new_list = []
        for num in val:
            new_list.append(num)
        result.append(new_list)

print(result)

# 92). Python program to create a dictionary from a sublist in a given list.
#Input: [[‘a’, 5], [‘b’, 8], [‘c’, 11], [‘d’, 14], [‘e’, 23]]
#Output: {‘a’: 5, ‘b’: 8, ‘c’: 11, ‘d’: 14, ‘e’: 23}
l92 = [['a', 5], ['b', 8], ['c', 11], ['d', 14], ['e', 23]]
result = dict(list(l92))
print(result)

# 93). Python program to replace ‘Java’ with ‘Python’ from the given list.
#Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
#Output: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Java’, ‘Its’, ‘Java’, ‘Language’]

l93 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
result = []
output = [word.replace("Python", "java") for word in l93]
print(output)
################################################
for word in l93:
    word= word.replace("Python", "java")
    result.append(word)
print(result)

# 94). Python program to convert the 3rd character of each word to a capital case from the given list.
#Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
#Output: [‘HelLo’, ‘stuDent’, ‘are’, ‘leaRning’, ‘PytHon’, ‘Its’, ‘PytHon’, ‘LanGuage’]
l94 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
output =[]
for word in l94:
    if len(word)>3:
        output.append(word[:3]+word[3].upper()+ word[4:])
    else:
       output.append(word)
print(output)
print("#"*40)
# 95). Python program to remove the 2nd character of each word from a given list.
#Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
#Output: [‘Hllo’, ‘sudent’, ‘ae’, ‘larning’, ‘Pthon’, ‘Is’, ‘Pthon’, ‘Lnguage’]

l95 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
output = []
for word in l95:
    output.append(word[:1]+word[2:])
print(output)

# 96). Python program to get a length of each word and add it as a dictionary from the given list.
#Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Language’]
#Output: [{‘Hello’:5, ‘student’: 7, ‘are’: 3, ‘learning’: 8, ‘Python’: 6, ‘Its’: 3, ‘Language’: 8}]
#Solution
l96 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Language']
dict = {}
list2 = []
for word in l96:
    dict[word] = len(word)
list2.append(dict)
print(list2)

# 97). Python program to remove duplicate dictionaries from the given list.
#Input: [{‘Hello’:5}, {‘student’: 7}, {‘are’: 3}, {‘learning’: 8}, {‘Hello’:5}, ,{‘Language’: 8}, {‘are’: 3}]
#Output: [{‘Hello’:5, ‘student’: 7, ‘are’: 3, ‘learning’: 8, ‘Python’: 6, ‘Its’: 3, ‘Language’: 8}]
l97 = [{'Hello':5}, {'student': 7}, {'are': 3}, {'learning': 8}, {'Hello':5}, {'Language': 8}, {'are': 3}]
list1 = {}
for data in l97:
    for key,val in data.items():
        list1[key] = val
print(list1)

# 98). Python program to decode a run-length encoded given list.
#Input: [[2, 1], 2, 3, [2, 4], 5, 1]
#Output: [1, 1, 2, 3, 4, 4, 5, 1]
list1 = [[2, 1], 2, 3, [2, 4], 5, 1]
list2 = []

for value in list1:
    if isinstance(value, list):
        list2.extend([value[1]] * value[0])
    else:
        list2.append(value)

print(list2)

# 99). Python program to round every number in a given list of numbers and print the total sum of the list.
#Input: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
#Output: 27
l99 = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
result = []
for val in l99:
    result.append(round(val))
list2 = sum(result)
print(list2)

# 100).  Python Program to get the Median of all the elements from the list.
l100 = [3,5,2,6,8,9]
l100.sort()
n = len(l100)

if n % 2 == 0:
    median = (l100[n//2 - 1] + l100[n//2]) / 2
else:
    median = l100[n//2]
print(median)