"""
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
list1.remove(10)
print(list1)
list1.remove('b')
print(list1)
list1.pop()
print(list1)
"""""
""""
list1=[10, 20, 30, 40]

for i in range(len(list1)):
    print( list1[i])
"""
"""
#  Python program to calculate the square of each number from the given list.
list2 = [10,20,30,40]
squarelist=[]
for i in range(len(list2)):
    x =list2[i] * list2[i]
    squarelist.append(x)
print(squarelist)
"""

""
# 5). Python program to find the minimum and maximum elements from the list.
"""
list2 = [10,20,30,40]
max=list2[0]
min=list2[0]
for i in range(len(list2)):
    if list2[i] > max:
        max = list2[i]
    if list2[i] < min:
        min = list2[i]
print("max",max)
print("min", min)
"""
"""
# 7). Python program to remove all duplicate elements from the list.
list = [10,20,40,10,20,20,40,50,10,50]
duplicatelist=[]
for i in range(len(list)):
    if list[i] not in duplicatelist:
        duplicatelist.append(list[i])

print(duplicatelist)
"""
list1 =[10,20,30,40,50]
evelist=[]
for val in list1:
    if val%2==0:
        evelist.append(val)
    else:
        continue
print(evelist)
#comprehension method
result=[x for x in list1 if x % 2==0]
print(result)
result2 = [x ** 2 for x in list1]

print(result2)
list1 = [5,10,15,20,25,30]
result3=[ (i,'even')if i%2==0 else (i, 'odd') for i in list1]

print(result3)
list2 = [10,20,40,10,20,20,40,50,10,50]
list2.sort()
print(list2)
list2.reverse()
print(list2)
print(dir(list))
list2 = ["p","n","t","s"]
list2.sort()
print(list2)