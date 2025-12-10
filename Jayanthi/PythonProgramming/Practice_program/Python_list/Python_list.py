print(dir(list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#append() Method
list1=[2,3,5,5+6j]
str='hello'
list1.append(str)
print(list1)

# Insert() method
list2=['joy',4,56,7]
list2.insert(3,'joy')
print(list2)

# extend() method
list3=['python','Programming']
list3.extend(str)
print(list3)

# index() Method
list4=[5,6,8,9,'fun','y']
print(list4.index('fun'))

# remove() Method
list5=[5,7,8,9,10]
list5.remove(10)
print(list5)

# Copy() Method
list6=list4.copy()
print(list6)

# clear() Method
list5.clear()
print(list5)

# pop() Method
list7=[7,8,10,'python']
var=list7.pop()
print(var)
print(list7)
list8=[8,9,67,'fun','python']
list8.pop(3)
print(list8)

# count() Method
list9=[1,2,8,4,5,]
var1=list9.count(5)
print(var1)

#Sort() Method
# accending
list9.sort()
print(list9)
# decending
list9.sort(reverse=True)
print(list9)

#reverse()
list10=[8,8,8989,'Fun']
list10.reverse()
print(list10)

# List concat
list_a=['a','b','c']
list_b=[10,20,20]
list_c=list_a+list_b
print(list_c)

# list Repeatation
list_x=[2,5,7]
print(list_x*5)

##### Max, Min, Sun ####
list_y=[50,100,200]
print("max value:",max(list_y))
print("min value:",min(list_y))
print("sum value:",sum(list_y))

# Ascii Value A-Z 65-90 a-z 97 -122
for i in range(97,123):
    print(chr(i),end=" ")
print()
print("ASCII a",ord(a))







