print(dir(set))
'''
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', 
'__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', 
'__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', 
'__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
'__subclasshook__', '__xor__',

'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
  'symmetric_difference_update', 'union', 'update']
'''
print()
print("-"*15,'Set',"-"*15)
s1={2,4.5,'python', True,44}
print(s1) # {'python', True, 2, 4.5, 44}

print()
###################################
print("-"*15,'Add Method',"-"*15)
s2={2,4.5,'python', True,44}
print("Original:", s2) # Original: {True, 2, 4.5, 'python', 44}
s2.add(6)
print("Add Method:", s2) # Add Method: {True, 2, 4.5, 'python', 6, 44}

print()
###################################
print("-"*15,'Update Method',"-"*15)

a1={1,3,4}
a2={3,5,6}
val=a1.update(a2)
print("First set post update:",a1) # First set post update: {1, 3, 4, 5, 6}
print("Second set post update:",a2) # Second set post update: {3, 5, 6}
print("Val post update:",val) # Val post update: None

print()
###################################
print("-"*15,'Clear Method',"-"*15)

s3={2,4.5,'python', True,44}
print("Original:", s2) # Original: {True, 2, 4.5, 6, 44, 'python'}
s3.clear()
print("Clear Method:",s3) # Clear Method: set()

print()
###################################
print("-"*15,'Shallow Method',"-"*15)

s4={2,4.5,'python', True,44}
print("Original:", s4) # Original: {'python', 2, True, 4.5, 44}
s5=s4
s4.add(55)
print("Copy Method s4:", s4) # Copy Method s4: {True, 2, 4.5, 'python', 55, 44}
s5.add('check')
print("Copy Method s5:", s5) # Copy Method s5: {True, 2, 4.5, 'python', 'check', 55, 44}

print()
###################################
print("-"*15,'Deep Copy Method',"-"*15)

s6={2,4.5,'python', True,44}
print("Original:", s6) # Original: {'python', 2, True, 4.5, 44}
s7=s6.copy()
s6.add('new')
print("Deep copy Method s6:", s6) #Deep copy Method s6: {True, 2, 'new', 4.5, 'python', 44}
s7.add('check')
print("Deep Copy Method s7:", s7) # Deep Copy Method s7: {True, 2, 'check', 4.5, 44, 'python'}

print()
###################################
print("-"*15,'Union Method',"-"*15)

a1={1,3,4}
a2={3,4,5}
val=a1.union(a2)
print("First set:",a1) # First set: {1, 3, 4}
print("Second set:", a2) # Second set: {3, 4, 5}
print("Union Method:", val) # Union Method: {1, 3, 4, 5}

print()
###################################
print("-"*15,'Difference Method',"-"*15)

a1={1,3,4}
a2={3,4,5}
val=a1.difference(a2)
print("First set:",a1) # First set: {1, 3, 4}
print("Second set:", a2) # Second set: {3, 4, 5}
print("Difference Method:", val) # Difference Method: {1}

print()
###################################
print("-"*15,'Symmetric Difference Method',"-"*15)

a1={1,3,4}
a2={3,4,5}
val=a1.symmetric_difference(a2)
print("First set:",a1) # First set: {1, 3, 4}
print("Second set:", a2) # Second set: {3, 4, 5}
print("Symmetric Difference Method:", val) # Symmetric Difference Method: {1, 5}

print()
###################################
print("-"*15,'Intersection Method',"-"*15)

a1={1,3,4}
a2={3,4,5}
val=a1.intersection(a2)
print("First set:",a1) # First set: {1, 3, 4}
print("Second set:", a2) # Second set: {3, 4, 5}
print("Intersection Method:", val) # Intersection Method: {3, 4}

print()
###################################
print("-"*15,'Discard Method',"-"*15)

a1={1,3,4}
val=a1.discard(3)
print("First set post discard:",a1) # First set post discard: {1, 4}
print("Discard Method:", val) # Discard Method: None

print()
###################################
print("-"*15,'Remove Method',"-"*15)

a1={1,3,4}
val=a1.remove(3)
print("First set post discard:",a1) # First set post discard: {1, 4}
print("Remove Method:", val) # Remove Method: None

print()
###################################
print("-"*15,'Pop Method',"-"*15)

a1={1,3,4}
val=a1.pop()
print("First set post pop:",a1) # First set post pop: {3, 4}
print("Pop Method:", val) # Pop Method: 1


