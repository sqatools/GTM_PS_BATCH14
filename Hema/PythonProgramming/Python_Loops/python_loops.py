#range(start, end value, step)
"""
->range output will include the start value and exclude end value in th output
-> default start value is 0 and step value is 1
"""
#print values from 1 to 10
for i in range(1, 10, 1):
    print(i)

print("_"* 50)
for i in range(1, 10, 2):# here step value is 2
    print(i)

print("_"* 50)
#print values in reverse order from 5 to 1
for i in range(5, 0, -1):
    print(i)

print("_"* 50)
for i in range(2, -6, -1):
    print(i)

print("_"* 50)
#no output with range
for i in range(10, 1,1):
    print(i)

print("_"* 50)
#-> default start value is 0 and step value is 1
for i in range(5):# range (0, 5, 1)
    print(i)
print("_"* 50)

#Apply loop on different datatypes
list1 =[2,4,3,5]
for val in list1:
    print(val)
print("_"* 50)

#Apply on tuple
tup1 = ('s', 'e', 3, 50)
for val in tup1:
    print(val)
print("_"* 50)

#Apply on string
str1 = "Python"
for char in str1:
    print(char)
print("_"* 50)

#Apply loop with if condition and get all even numbers from given list
list2 =[12, 53, 74,89, 1]
for val in list2:# val does not pick value by indexing but just by position
    if val%2 == 0:
        print(val)
print("_"* 50)
#Without if condition also we can print even numbers
for j in range(10, 16, 2):
#if we want to print values in single line use end= " " because by default is end="/n"
    print(j, end=",")
print("_"* 50)
###################################################

#Nested loop condition
#Address :outer loop
for i in range(1,10, 1):
    print("Address: i=", i)
    # Package: inner loop
    for j in range(1, 4,1):
        print("package: j=", j)



