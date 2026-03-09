# Apply Loop on a set
print("Apply Loop on a set")

s1={2,3.4,'python',3}
for val in s1:
    print(val)
'''
3.4
2
3
python
'''
print()
################################################
print('-'*15,'Program 1','-'*15)
print('Get all the even values from set.')

set3 = {3, 5, 7, 8, 9, 10, 11}
set5 = set()

for val in set3:
    if val%2==0:
        set5.add(val)
    else:
        continue
print("Even Numbers are:",set5) # Even Numbers are: {8, 10}

print()
################################################
print('-'*15,'Program 2','-'*15)
print(' write a python program to get all the values which are divisible by 3 and 5 from set.')

set3 = {3, 5, 7, 8, 9,30, 10, 11,15}
set5 = set()

for val in set3:
    if val%3==0 and val%5==0:
        set5.add(val)
    else:
        continue
print("Divisible by 3 and 5 Numbers are:",set5) # Divisible by 3 and 5 Numbers are: {30, 15}

print()
################################################
print('-'*15,'Program 2','-'*15)
print('Move data from one set to another.')

set_x = {6, 7, 8, 3, 16, 12}
set_y = set()

for val in range (len(set_x)):
    a1=set_x.pop()
    set_y.add(a1)
print("set_x :",set_x) # set_x : set()
print("set_y :",set_y) # set_y : {3, 6, 7, 8, 12, 16}



