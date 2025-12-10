list1 = [10, 20, 30, 40]
print(list1[-1])
print(list1[3])
print(list1[0])
print(list1[::-1])
list2 =[10, "nalini", True, ('a', 'b', 'c'), {1, 2, 3, 4}]
print(list2)
print(list2[1][2])
list1.append(50)
print(list1)
list1.insert(5,60)

print(list1)
list1.insert(1, 10.5)
print(list1)
list3 = [70,80,90,100]
list4=['a','b','c','d','e']
list1.extend(list3)
print(list1)
list1.extend(list4)
print(list1)