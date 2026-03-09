print(dir(set))

#'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop',
# 'remove', 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update']

# Add this method add data to set in random order
print("-"*50)
set2={2,3,5,6,7}
set2.add(30)
print("set2:",set2)
print("-"*50)
#Update method
set3 ={5,7,9,20,10}
set4={'a','b','c'}
set3.update(set4)
print("set3:",set3)
print("set4:",set4)
print('-'*50)
# union method combine 2 set data and generator new set as output
set3 ={5,7,9,20,10}
set4={'a','b','c'}
set5=set3.union(set4)
print("set3:",set3)
print("set4:",set4)
print("Set5:",set5)

print('-'*50)
#remove method this used to remove any specific value from set

set6 ={5,7,9,20,10}
set6.remove(20)# keyerror when no set has that value
print(set6)

print('-'*50)
#discard method this used to remove any specific value from
# set but when non exciting value no key error as remove methos

set7 ={5,7,9,20,10}
set7.discard(30)
print(set7)

print('-'*50)
#diferent method this used to different between 2 set

set8 ={5,7,9,20,10}
set9 ={5,7,'a','b'}
val=set9.difference(set8)
print("Diference on set :",val)

print('-'*50)
#intersection method this used to common between 2 set

set10 ={5,7,9,20,10}
set11 ={5,7,'a','b'}
val=set10.intersection(set11)
print("common on set :",val)

#Symentric difference difference of both the set together
print('-'*50)
set12 ={5,7,9,20,10}
set13 ={5,7,'a','b'}
val=set12.symmetric_difference(set13)
print("symmetric difference :",val)

# Copy
#Shallow copy : when one set is assign to other set
# and modify value in any of the set then changes will
# reflect in both the set
print('-'*50)
set14 ={5,7,9,20,10}
set15 = set14
set15.add(50)
set14.add(30)
print("Set15:",set15)
print("Set14:",set14)
# Deep copy , we will copy method explicitly
print('-'*50)
set16 ={5,7,9,20,10}
set17 = set16.copy()
set16.add(50)
set17.add(30)
print("Set16:",set16)
print("Set17:",set17)
print('-'*50)
#Pop method
set_c={200,300,500,100}
val=set_c.pop()
print("Val:",val)
print("Set_c",set_c)

print('-'*50)
#Clear
set_d={200,300,500,100}
set_d.clear()
print("Set_d",set_d)

#Loop concept in set

set_f={5,7,9,2,12}
for val in set_f:
    print(val)

#frozen set will freeze all the value and no modification
print('-'*50)
list1=[6,6,7,9,8,9]
frozen_set=frozenset(list1)
print("List1:",list1)
print("Fronzon_set:",frozen_set)

#Get the even value
print('-'*50)
set5={2,3,5,6,7,7,8,10,9}
set6=set()
for i in set5:
    if i%2==0:
        set6.add(i)
    else:
        continue
print(set6)

# Write a python program to get all the value which are divisible by 3 and 5
Set_div={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
Set_3_5=set()
Set_3=set()
Set_5=set()
for i in Set_div:
    if i%3==0 and i%5==0:
        Set_3_5.add(i)
    elif i%3==0:
        Set_3.add(i)
    elif i%5==0:
        Set_5.add(i)
    else:
        continue
print("Set_ans dic by 3 and 5:",Set_3_5)
print("Set div by 3:", Set_3)
print("Set div by 5:",Set_5)

print('-'*50)
# Move data from one set to another
set_x={6,7,8,3,16,12}
set_y=set()
#output:
#set_x=set()
#Set_Y={6,7,8,3,16,12}

for i in range(len(set_x)):
    val=set_x.pop()
    set_y.add(val)
print("set_y:",set_y)
print("set_x:",set_x)


