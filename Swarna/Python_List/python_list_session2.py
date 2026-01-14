#sort() method
list_1 = [50, 10, 70, 30, 90, 20]
list_1.sort()
print("list_1 :", list_1)  # [10, 20, 30, 50, 70, 90]

list_2 = [50, 10, 70, 30, 90, 20]
list_2.sort(reverse=True)
print("list_2 :", list_2)  # [90, 70,

list_a = ['Hello', 'we', 'are', 'learning', 'Python', 'Polo']
list_a.sort()
print("list_a :", list_a)  # ['Hello', 'Polo', 'Python', 'are', 'learning', 'we']

print("#" * 50)
################################
# reverse() method : This method reverse list data and modify the original list.

list_3 = [6, 2, 7, 1, 3, 5, 20, 30]
list_3.reverse()
print("list_3 :", list_3)  # [30, 20, 5, 3, 1, 7, 2, 6]

print("#" * 50)
################################
# count() method : This method count the number of occurrences of any given value

list_4 = [6, 12, 7, 1, 3, 5, 20, 12, 30, 7, 12]
print("count of 12 :", list_4.count(12))  # count of 12 : 3

print("#" * 50)
################################
# index() method : This method return the index of given value

list_5 = [6, 12, 7, 10, 300, 500, 20, 12, 30, 7, 12]
print("index of 500 :", list_5.index(500))  # index of 500 : 5

print("#" * 50)
################################
# clear() method : This method clear all data from list and remain empty list.

list_6 = [6, 12, 7, 10, 300, 500, 20, 12, 30, 7, 12]
list_6.clear()

print("list_6 :", list_6)  # list_6 : []

print("#" * 50)
############################################################
# list concatenation :  combine two list data with plus operation without changing the original list

list_a = ['a', 'b', 'c']
list_b = [10, 20, 30]
list_c = list_a + list_b
print("list_c :", list_c)  # ['a', 'b', 'c', 10, 20, 30]

# list repetition :  when we multiply list with any number, then it will repeat the list values that numbers of
# time.

list_x = [2, 5, 7]
print(list_x * 5)  # [2, 5, 7, 2, 5, 7, 2, 5, 7, 2, 5, 7, 2, 5, 7]

print("#" * 50)
############### Max, Min, sum #############

list_y = [50, 60, 30, 12, 16]
print("Max value:", max(list_y))  # Max value: 60
print("Min value :", min(list_y))  # Min value : 12
print("Sum of values :", sum(list_y))  # Sum of values : 168

list_z = ['abc', 'hello', 'Python', 'Programming']
print(max(list_z))

# ASCII VALUES
# A-Z : 65- 90
# a -z : 97 - 122

for i in range(65, 91):
    print(chr(i), end=" ")
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
print()

for j in range(97, 123):
    print(chr(j), end=" ")

# a b c d e f g h i j k l m n o p q r s t u v w x y z

print("_" * 50)
# ord() function :  this function return ASCII of value of character
print("ASCII of a:", ord('a'))  # ASCII of a: 97

print("_"*50)
###################################################################
# Q1 : write a python program to get all even values from list
list1 = [4, 5, 7, 8, 12, 17, 56]
#output = [4, 8, 12, 56]

output = []

for val in list1:
    print(output)
    if val%2 == 0:
        output.append(val)
    else:
        continue

print("Output :", output) # [4, 8, 12, 56]

print("_"*50)
# solution with List comprehension
result = [x for x in list1 if x%2 == 0]
print("result :", result) # [4, 8, 12, 56]

print("_"*50)
########################################################
# Q2 : write a python program to get all even and odd values with tag from list
list1 = [4, 5, 7, 8, 12]
# result = [(4, 'even'), (5, 'odd'), (7, 'odd'), (8, 'even'), (12, 'even')]

result = []
for val in list1:
    if val%2  == 0:
        result.append((val, 'even'))
    else:
        result.append((val, 'odd'))

print("result :", result)

print("-"*50)
# solve same program with list comprehension
result2 = [(y, 'even') if y%2 == 0 else (y, 'odd') for y in list1]
print("result2 :", result2)


print("_"*50)
# get square of all value
list_2 = [5, 7, 8, 2, 9]
square = [x**2 for x in list_2]
print("square of values :", square)
# [25, 49, 64, 4, 81]