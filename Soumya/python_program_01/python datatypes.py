
list1 = [4, 3.6, 3+50j, 'Hello', [5, 6, 6], (6, 5, 7), {'x': 123}, {12, 7, 12}, False]
print(list1, type(list1))

list2 = [66, 6, 10, 12, 50]
print(list2[3])
print(list2[-2])
print("_"*30)

list3 = [25, 3.5, 3+40j, 'Hello', [53, 9, 60], (11, 15, 17), {'a': 123}, {5, 7, 8}, False]
print(list3[4])
print(list3[4][2])
print(list3[2])
print(list3.index(False))

list4 = [60, 18, 29, 200]
print("list4 :", list4)
print("_"*60)

###### Tuple ####
tup1 = (2, 3.5, 2+3j, 'PyCharm', [33, 7, 10], (10, 6, 4), {'a': 123}, {20, 30, 20}, False, "Yesterday's")
print(tup1, type(tup1))

print(tup1[3])
print(tup1[-3])
print(tup1[-1])
print(tup1[-2+1])


print("_"*50)
####### Dictionary #####
dict1 = {'a': 123, 5: 'Python', 4.5: [30, 50, 70]}
print(dict1, type(dict1))
print(dict1['a'])

dict1['a'] = 200
dict1['b'] = 100

print("dict1 :", dict1)

dict2 = {200: 'Hello',
         7.5 : [50, 6, 7],
         45+5j: (16, 19, 50),
         'abc': {'a': 123, 'b': 876},
         (11, 20, 30): {6, 4, 5, 11, 21},
         True: 345,
         }

print(dict2)
print("_"*60)


a = 30
b = 50
c = 30
print(a == b) # False
print(a == c) # True



P=int(input("Enter principal amount:"))
R=float(input("Enter rate of interest:"))
T=int(input("Enter time in years:"))
SI=(P*R*T)/100
print("Simple Interest is:",SI)
