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
