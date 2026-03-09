"""
# Properties:
-> List is mutable data type, that we can modify any point of time.
-> List can contain any types of data, int, float, complex, str, list, tuple, dict, set, boolean.
-> List follows positive negative indexing as like string.
-> We define list with square bracket.
"""
list1 =[1,2.5 , [10,20,30], "hello", 4+6j, True, {100,200,300}, (12, 54,95), {'a':4,'b':6}]
print(list1, type(list1))#<class 'list'>

# Get data from list using index
print(list1[3])#hello
print(list1[3][1])#e

# get child list from given list
print(list1[2][2])#30
print(list1[-1]['b'])#6

print("_"*10)
# Apply loop on the list
list2= [11,22,33,54]
for h in list2:
    print(h)

for i in range(len(list2)):
    print((i, list2[i]))

'''x = '33'
if x in list2:
    print(x)'''


######################## slicing in list ######################
"""
# Rule1 : list[start index:  end index]

->  In this rule it will always get output from left to right.
->  default start index value is 0
->  default end index value is end of list.
->  start index and end index could be positive negative.
->  Output will include the start index value and exclude end index value

# Rule2 : list[start index:  end index: step value]

-> In this rule, output will include start index value and exclude end index value
-> default start index is zero (0) if step value is +ve
-> default start index is -1 if step value is -ve
-> default end index will be end of list if step value is +ve
-> default end index will be start of list if step value is -ve

"""
list3 = [4, 7, 12, 50, 70, 33, 21]
print(list3[0:4])  # [4, 7, 12, 50]
print(list3[3:7]) # [50, 70, 33, 21]
print(list3[0:7:2]) # [4, 12, 70, 21]
print(list3[-2:-6:-1]) # [33, 70, 50, 12]
print(list3[-1:-8:-1]) # [21, 33, 70, 50, 12, 7, 4]
print(list3[::-1])  # [21, 33, 70, 50, 12, 7, 4]

print("_"*50)
######################## List Methods #####################
print(dir(list3))
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
##################
# append() method :  This method add data to the list at the end of the list.
list_a= [12, 53, 7, 864, 96]
list_a.append(1000)
print(list_a)

# insert() method : this method add data to the list at specific index position.

list_a.insert(2, 'hello')
print(list_a)
list_a.insert(3, 999)
print(list_a)


print("_"*50)
##################
# extend() method :  this method add one list data to another list

list_b =[ 'my', 'world']
list_a.extend(list_b)
print(list_a)

str1 = 'hello'
list_f = [1, 2, 3]
list_f.extend(str1)
print("list_f :", list_f)# [1, 2, 3, 'h', 'e', 'l', 'l', 'o']
print("_"*50)

dict1= {'a': 123, 'b': 567}
list2 = [5, 67, 8]
list2.extend(dict1)
print("list2 :", list2) # [5, 67, 8, 'a', 'b']
##################
# remove() method:  this method remove any specific data from list
#                   -> if value is repeated multiple times, then it will remove first occurrence

list_c= [1,2,3,4,3,2]
list_c.remove(3)
print(list_c)#[1, 2, 4, 3, 2]

# pop() method :  This method remove data from specific index position and return the value.
#                 default index position is -1
list_d= [12, 63, 6433, 73]
# remove from specific index
v1= list_d.pop(2)
print("removed value :",v1)#removed value : 6433
print("list_d: ",list_d)#list_d:  [12, 63, 73]

# remove from default index -1
v2= list_d.pop()
print("removed value :",v2)#removed value : 73
print("list_d: ",list_d)#list_d:  [12, 63]