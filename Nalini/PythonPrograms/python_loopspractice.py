"""
 Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *

"""
"""
for i in range(1, 7):
    for j in range(1, i):
        print (" * ", end=" ")
    print( )
print()

"""
"""
for i in range(7, 1,-1):
    for j in range(1, i):
        print (" * ", end=" ")
    print( )
print()
"""
"""
Python Loops program to count the number of even and odd numbers from a series of numbers using python.
"""
"""
count=0
oddcount=0
for i in range(1, 21):
    if(i%2==0):
        print(i)
        count+=1
    else:
        oddcount+=1

print("even numbers bwt 1 to 20:", count)
print("odd numbers bwt 1 to 20 :", oddcount)
"""
"""
6). Write a program to get the Fibonacci series between 0 to 20 using python.
"""
a = 0
b = 1

for i in range(0, 20):
    if i == 0:
        print(a, ",", end=" ")
    elif i == 1:
        print(b, ",", end=" ")
    else:
        fib = a + b
        print(fib, ",", end=" ")
        a = b
        b = fib





