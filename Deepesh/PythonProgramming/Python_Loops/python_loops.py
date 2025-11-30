# range(start, end value, step)
"""
->  range output will include the start value and exclude end value in the output
->

"""
# print values from 1 to 10
for i in range(1, 11, 1):
    print(i)


print("_"*40)
# print values from 1 to 10 with step value 2
for i in range(1, 10, 2):
    print(i)


print("_"*40)
# print value in reverse order from 5 to 1
for i in range(5, 0, -1):
    print(i)

"""
5
4
3
2
1
"""

print("_"*40)
# print value in reverse order till -5
for i in range(2, -6, -1):
    print(i)

"""
2
1
0
-1
-2
-3
-4
-5

"""


print("_"*40)
# No output with range if values are not in range
for i in range(10, 1, 1):
    print(i)


print("_"*40)
# default start value is zero and default step value 1
for j in range(5): # range(0, 5, 1)
    print(j)


print("_"*40)
# Apply loop of different data types:
list1 = [5, 7, 8, 2, 5, 18]

for val in list1:
    print(val)

print("_"*40)
# Apply loop on tuple
tup1 = ('a', 'b', 'c', 234)
for val in tup1:
    print(val)


print("_"*40)
# Apply loop on string
str1 = "Programming"
for char in str1:
    print(char)

print("_"*40)
# write loop with if condition and get all even number from given list

list2 = [5, 7, 9, 2, 13, 14]
for val in list2:
    if val%2 == 0:
        print(val, end=" ")

###################################
print()
print("_"*40)
for i in range(6, 14, 2):
    print(i)


print("_"*40)
#########################################################
# Nested loop condition.

# Address: outer loop
for i in range(1, 6, 1): # i = 1, 2, 3, 4, 5
    print("Address : i=",i)
    # package : inner loop
    for j in range(1, 4, 1): # j = 1, 2, 3
        print("Package : j=", j)

    print("_"*20)


print("_"*40)
#########################################################
# While loop condition.






