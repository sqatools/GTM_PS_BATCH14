#print number from 1 to 6
"""""
a = 1
while a <= 6:
    print(a)
    a = a+1

print("_"*40)

#print all odd numbers till 20

b = 1
while b <= 10:
    if b % 2 != 0:
        print(b)
        b += 1

"""""

print("_"*40)

####################### Continue and break statment ######################

# print values from 1 to 10 with continue statement

v1 = 1
while v1 <= 10:
    if v1 in [1, 9]:
        v1 += 1
        continue

    print(v1)
    v1 += 2

print("_"*50)

# break statement:
# #once the code is satisfied with break condition then loop will terminate immediately.

m1 = 1
while m1 <= 10:
    if m1 in [4, 8]:
        continue
    print(m1)
    m1 += 1













