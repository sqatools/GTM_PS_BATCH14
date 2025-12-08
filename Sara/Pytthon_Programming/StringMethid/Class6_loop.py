################ Apply loop on string ###############
s1 = "Learning Python"
# loop without indexing
for char in s1: # char will give all char. if u write i it will print s1 value multiple time
    print(char)
print("-"*40)
'''
L
e
a
r
n
i
n
g
 
P
y
t
h
o
n
'''
# loop with indexing
s1 = "Learning Python"
for i in range(0,len(s1),1):
    print(i)
print("-"*40)
'''
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
'''
# loop with indexing
s1 = "Learning Python"
for i in range(0,len(s1),1):
    print(i, s1[i])
"""
#this will also give same output as above
print("_"*50)
for i, char in enumerate(s1):
    print(i, char)
"""
'''
0 L
1 e
2 a
3 r
4 n
5 i
6 n
7 g
8  
9 P
10 y
11 t
12 h
13 o
14 n
'''
