#************** DICTIONARY *******************
print("-"*15, "Dictionary", "-"*15)

'''
D1={'a':45, '3.3': 33, '45+6j':111, '4': 55, (1,3,5): 56,{1,2,3}:22, {'a':44}: 21, True: 67}
print(D1) #TypeError: cannot use 'set' as a dict key (unhashable type: 'set')

D1={'a':45, 3.3: 33, '45+6j':111, '4': 55, (1,3,5): 56,'c':22, {'a':44}: 21, True: 67}
print(D1)
#TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
'''
#Mutable datatype (list,dict and set) cannot be used as key. Value can be any datatype.
D1={'a':45, 3.3: 33, '45+6j':111, '4': 55, (1,3,5): 56,'c':22, 'd': 21, True: 67}
print(D1) #{'a': 45, 3.3: 33, '45+6j': 111, '4': 55, (1, 3, 5): 56, 'c': 22, 'd': 21, True: 67}
print(type(D1)) #<class 'dict'>
print("")

#************** Update/Add key value *******************
print("-"*15, "Update/Add key value", "-"*15)

D2={'check':45, 3.3: 33, '45+6j':111, 4: 55, (1,3,5): 56,'c':22, 'd': 21, True: 67, 'r': 4}
print(D2) #{'check': 45, 3.3: 33, '45+6j': 111, 4: 55, (1, 3, 5): 56, 'c': 22, 'd': 21, True: 67, 'r': 4}
print("")

D2[3.3]="updated"
print(D2) #{'check': 45, 3.3: 'updated', '45+6j': 111, 4: 55, (1, 3, 5): 56, 'c': 22, 'd': 21, True: 67, 'r': 4}
print("")

D2['new']=0.0
print(D2) #{'check': 45, 3.3: 'updated', '45+6j': 111, 4: 55, (1, 3, 5): 56, 'c': 22, 'd': 21, True: 67, 'r': 4, 'new': 0.0}
print("")

#************* SET ********************
print("-"*15, "SET", "-"*15)
'''
s1={1,2.2,4+7j,"Hello",[1,4,5],(5,4),{'e':77},{3,6,4},False}
print(s1)
#TypeError: cannot use 'list' as a set element (unhashable type: 'list')

s1={1,2.2,4+7j,"Hello",(5,4),{'e':77},{3,6,4},False}
print(s1)
#TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')

s1={1,2.2,4+7j,"Hello",(5,4),{3,6,4},False}
print(s1)
#TypeError: cannot use 'set' as a set element (unhashable type: 'set')
'''
# List, Dict, Set cannot be used as value for set since those are mutable.

s1={1,2.2,4+7j,"Hello",(5,4),False}
print(s1) #{False, 1, 2.2, (4+7j), (5, 4), 'Hello'}
print(type(s1)) #<class 'set'>

#*** Store only unique value and in random order**********
s2={'Hi', 3, 66.5,5,3}
print(s2) #{66.5, 3, 5, 'Hi'}
print("")
#********************** BOOLEAN ****************************
print("-"*15,"BOOLEAN","-"*15)

b1=57
b2=44
b3=57
print(b1==b2) #False
print(b1==b3) #True
