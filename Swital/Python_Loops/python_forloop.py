# Start with simple for loop syntax
# for i in range(start_value, end_value, step[increase and decrease])
# print 1 to 15
print("#" * 50)
for i in range(1, 15, 1):
    print(i)

# print 1 to 15 with step value 2 means increase by 2 alternate value
print("#" * 50)
for i in range(-50, 10, -2):
    print(i)

# print -50 to 10
for i in range(-50, 10, 1):
    print(i)
# other way
print("#" * 50)
for i in range(10, -50, -1):
    print(i)

# print -50 to 10 with step value 2 means increase by 2 alternate value
print("#" * 50)
for i in range(-50, 10, 2):
    print(i, end="")
# print only even numbers from 1 to 50
print("#" * 50)
for i in range(2, 50, 2):
    print(i, end="")

############################# String ################################################
print("#" * 50)
str2 = "AutomationTest"
for val in str2:
    print(val)

############################# List ################################################

print("#" * 50)
list1 = [3, 5, 1, 5, 1, 5, 6, 7, 8]
for val in list1:
    print(val)

############################# tuple ################################################

print("#" * 50)
tup1 = (3, "hi", 50 + 3j, [1, 2, 3])
for val in tup1:
    print(val)

# WAP to get even number from list using if condition
print("#" * 50)
list2 = [3, 4, 2, 5, 6, 2, 5, 7, 8, 12]
for val in list2:
    if val%2==0:
        print(val)

############################Nested Loop#####################################
print("#" * 50)
for i in range(4):
    print(" i range value: ", i)
    for j in range(3):
        print(" j range value: ", j)

    print("#" * 30)


############################ While Loop ####################################
print("#" * 50)
n = 1
while n <= 5:
    print(n)
    n += 1

############################ Continue Statement ####################################
print("#" * 50)
n = 1
while n <= 10:
    if n == 2:
        n += 1
        continue
    print(n)
    n += 1

############################ Break Statement ####################################
print("#" * 50)
n1 = 1
while n1 <= 10:
    if n1 == 3:
        break
    print(n1)
    n1 += 1