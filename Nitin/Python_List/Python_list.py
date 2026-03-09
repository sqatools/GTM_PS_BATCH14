list1=[2, 3.5, 5+7j, 'Hello', [4, 6, 8], (1, 3, 5), {'a': 123, 'b': 125}, {4, 6, 7}, True]
print("list1:",list1)

# Get data from list using index
print(list1[0])       #2
print(list1[4])       #[4, 6, 8]

# get child list from given list
print(list1[4])      #[4, 6, 8]
print(list1[4][0])   #4
print("get the child list from list using the -ve index")
print(list1[-5][-1])
print(list1[-5][-3])

print("---"*50)

print(list1[-1])      #True
print(list1[-2])      #{4, 6, 7}
print(list1[-5])      #[4, 6, 8]
print(list1[-5][-1])  #8
print(list1[-5][-3])  #4
print(id(list1))      #2365697905736
print(type(list1))    #<class 'list'>

print("---"*50)
##################################################
# Apply loop on the list
##################################################
list2 = ['a', 'b', 'c', 'd']
for i in list2:         # 'a','b','c'
    print(i, end=":")
    print(list2.index(i))


'''
    print(i, list2[i])   # Index are number but here we are giving the index string
   TypeError: list indices must be integers or slices, not str
'''
print("---"*50)
for i in range(len(list2)): # 0,1,2,3
    print(i,list2[i])       #0a

print("---"*50)
 #        0  1   2   3   4   5   6
list3 = [4, 7, 12, 50, 70, 33, 21]
 #      -7  -6 -5  -4  -3  -2  -1

print(list3[0:4])        # 4,7,12
print(list3[3:7])        # 50,70,33,21
print(list3[0:7:2])      # 4,12,70,21
print(list3[-2:-5:-1])   # 12,50,70,33   [33, 70, 50, 12]
#           st stp stpu(r->l)
print(list3[-1:-8:-1])    #21,33,70,50,12,7,4
#          ssa1:ssa2:r->l
print(list3[::-1])

print(list3[-6:4])

print(list3[-6:-2:-1])

print("_"*50)
######################## List Methods #####################
print(dir(list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("_"*50)
######################## List Methods #####################
# append() method :  This method add data to the list at the end of the list.
list_a = [5, 7, 9, 10, 21]
list_a.append(100)
print(list_a)
list_a.append("Python")
print(list_a)


print("_"*50)
##################
# insert() method : this method add data to the list at specific index position.
list_b = [6, 7, 8, 10, 30, 40]
list_b.insert(2, 100)
print("list_b :", list_b) # list_b : [6, 7, 100, 8, 10, 30, 40]

print("_"*50)
##################
# extend() method :  this method add one list data to another list
list_c = ['a', 'b']
list_d = [11, 22, 33, 44]
list_d.extend(list_c)
print(list_d)   #[11, 22, 33, 44, 'a', 'b']

str1="helo"
list_f=[1,2,3,4]
list_f.extend(str1)
print(list_f)

dict1={'a':123,'b':321,'c':000}
list_g=[1,2,3,4]
list_g.extend(dict1)
print(list_g)

print("_"*50)
##################
print("_"*50)
##################
# remove() method:  this method remove any specific data from list
#                   -> if value is repeated multiple times, then it will remove first occurrence

list_x = [10, 20, 30, 20, 30, 60]
list_x.remove(20)
print(list_x)
#list_x.remove(0)
##################
# pop() method :  This method remove data from specific index position and return the value.
#                 default index position is -1

list_y = ['a', 'b', 'c', 'd', 'f', 'b']
#print(list_y.pop(10)) #IndexError: pop index out of rangeprint(list_y)


################################
# sort() method : This method sort list data in ascending and descending order.
#                 This method will update the original list

print("---"*10)
list_11 = [16, 22, 7, 1, 3, 5]
list_11.sort()   # sort() method return None
print("Ascending of list:",list_11)

print("---"*10)
list_11.sort(reverse=True)
print("Desending of list:",list_11)


print("#" * 50)
################################
# reverse() method : This method reverse list data and modify the original list.

list_21=[2,3,9,8,5,6,2,1]
list_21.reverse()
print("Reverse a list:",list_21) #Reverse a list: [1, 2, 6, 5, 8, 9, 3, 2]

print("#" * 50)
################################
# count() method : This method count the number of occurrences of any given value
list_23=[2,3,4,5,6,2,3]
print(list_23.count(3))

################################
# index() method : This method return the index of given value
list_23=[2,3,4,5,6,2,3]
print("index/1st occurance of i :",list_23.index(4))

print("#" * 50)
################################
# clear() method : This method clear all data from list and remain empty list.
list_24 = [6, 12, 7, 10, 300, 500, 20, 12, 30, 7, 12]
list_24.clear()
print(list_24)

# list concatenation :  combine two list data with plus operation without changing the original list
