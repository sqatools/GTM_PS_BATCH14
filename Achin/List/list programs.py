#1 square of each number from list
#numbers=[12,23,45]

#for i in range(len(numbers)):
 #   print(numbers[i]*numbers[i])

#2 combine 2 list
'''
list1=[1,2,3]
list2=[4,5,6]

list3=list1+list2
print(list3)
'''
from Nalini.PythonPrograms.python_listprogams import duplicatelist

#3
'''
list1=[1,2,3,78,89,120]
#print(sum(list1))
sum=0
for x in list1:
    sum=sum+x
print(sum)
'''

#product of numbers
'''
list1=[11,7,2,3,4]
mul=1
for x in list1:
    mul=mul*x
print(mul)
'''

#remove duplicate elements
list1=[11,11,34,34,67,34,66,90,12]
duplicatelist=[]
count=1
for x in list1:
    if x not in duplicatelist:
        duplicatelist.append(x)
    else:
        continue
print(duplicatelist)

#print list whose sum is 10





