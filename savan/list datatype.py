list1 = [2, 3.7, 3+30j, 'Hello', [3, 5, 6], (1, 5, 7), {'a': 123}, {5, 7, 8}, True]
print(list1)
print(list1[2])
print(list1[4][0])
list1.append([91,2,3])
print(list1)

############################
Tuple1=(1,2.3,4+4J,'savan',[2,3,'dinesh'],(2.4,7),{'s':'we'},{7,8,6},False)
print(Tuple1)
print(Tuple1[1])
###########################
dict1={2:2,
       2.1:2.1,
       'savan':'ponarkar',
       2+3j:5+3j,
       (2,3,4):(4,5,3),
       (3,4,1):['SAC',2,3.1],
       6:True}
print(dict1)

dict1[2]='sam'
print(dict1)

##########################################################
#set

#sorting it will perform
#only immutable datatypes
set1={12, 13, 12, 5, 'Python', (4, 6, 8), True, 5.7, 7+34j, 5}
print(set1)
########################
#boolean
a = 30
b = 50
c = 30
print(a == b) # False
print(a == c) # True