print(dir(tuple))
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

'''
print()
######################################
print("-"*15,'Example',"-"*15)
t1=(1,2.3,5+7j,{3,4,5},(4,5))
print(t1) # (1, 2.3, (5+7j), {3, 4, 5}, (4, 5))

print("Value using indexing:", t1[2]) # Value using indexing: (5+7j)
print("Value using slicing:", t1[3::]) # Value using slicing: ({3, 4, 5}, (4, 5))

print()
################## Count() Method ####################
print("-"*15,'Count() Method',"-"*15)
t2=(1,2,3,4,3,6,3,7)
print('total occurrence of 3 is:', t2.count(3)) # total occurrence of 3 is: 3

t3=('a','Hi',3,4,'a','abc')
print('total occurrence of a is:', t3.count('a')) # total occurrence of a is: 2

print()
################## Index() Method ####################
print("-"*15,'Index() Method',"-"*15)
t4=(1,'Hello',4.4,5+7j,{3,4,5},(4,5),'World')
print('index position of value Hello:',t4.index('Hello')) # index position of value Hello: 1
print('index position of value (4,5):',t4.index((4,5))) # index position of value (4,5): 5

print()
################## Repetition function ####################
print("-"*15,'Repetition',"-"*15)
t5=(1,'Hello',4.4,5+7j,{3,4,5},(4,5),'World')
print('Twice of tuple is:', t5*2)# (1, 'Hello', 4.4, (5+7j), {3, 4, 5}, (4, 5), 'World', 1, 'Hello', 4.4, (5+7j), {3, 4, 5}, (4, 5), 'World')

print()
################## Concatenation function ####################
print("-"*15,'Concatenation',"-"*15)
t6=(4,5,6)
t7=(4,'a',7)
print('Concatenation of 2 tuple:', t6+t7) # Concatenation of 2 tuple: (4, 5, 6, 4, 'a', 7)

print()
################## Max, Min and Sum function ####################
print("-"*15,'Max, Min and Sum',"-"*15)
t8=(4,5,3,70,3)
print('Max value is:',max(t8)) # Max value is: 70
print('Min value is:',min(t8)) # Min value is: 3
print('Sum value is:',sum(t8)) # Sum value is: 85