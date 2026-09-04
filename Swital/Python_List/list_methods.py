list2 = [3,4,1,3,2,1,4,2]
# Append method
list2.append(8)
list2.append(9)
print("Append method list: ", list2)

# Insert method
list2.insert(5,6)
list2.insert(0,1)
print("Insert method list: ", list2)

# Extend method
list3 = [7,8,4]
list2.extend(list3)
print("Extend method list: ", list2)

# Remove method
list2.remove(3)
print("Remove method list: ", list2)

# Pop method
list2.pop()
print("Pop method list: ", list2)
list2.pop(6)
print("Pop method list at 6th index: ", list2)

# Sort Method
list2.sort()
print("Ascending order: ", list2)
list2.sort(reverse=True)
print("Descending order: ", list2)

# Reverse Method
list3 = [4,2,5,3,5,2,1,5,7,9]
list3.reverse()
print("Reverse order: ", list3)

# Count Method
print("Count of 2 : ", list3.count(2))

# Index Method
print("Index of 5 : ", list3.index(5))

# Clear Method
list3.clear()
print("Count of 2 : ", list3)

# Concatenation Method
list1 = ['a', 'b', 'c']
list2 = [2,4,6]
list3 = list1+list2
print("Concate Method: ", list3)

# Repeat Method
list_1 = [2,3,5]
print("Repeat method: ", list_1*3)

#Min, Max, Sum function
list3 = [4,2,5,3,5,2,1,5,7,9]
print("Max value: ", max(list3))
print("Min value: ", min(list3))
print("Sum value: ", sum(list3))


# Program for Even Number
list4 = [3,5,4,6,8,7,1]
output = []
for val in list4:
    if val % 2 == 0:
        output.append(val)
    else:
        continue
print(output)

# list comprehension
result = [num for num in list4 if num % 2 ==0 ]
print(result)

# Program for value print along with string
list_a = [2,3,4,6,5]
output = []
for val in list_a:
    if val % 2 == 0:
        output.append((val, 'Even'))
    else:
        output.append((val, 'Odd'))
print(output)
