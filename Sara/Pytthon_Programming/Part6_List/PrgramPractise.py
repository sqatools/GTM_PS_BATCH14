#******************* Program 1 ***************************************
print('-'*15,"Program 1", '-'*15)
# Write a python program to get all the even number from the list
l1=[4,5,7,8,12,17,56]
l2=[]

for val in l1:
    if val%2==0:
        l2.append(val)
    else:
        continue
print("Even values:",l2) # Even values: [4, 8, 12, 56]

# solution with List comprehension
result = [x for x in l1 if x%2 == 0] # if there is only if condition we write code on the right
print("result :", result) # [4, 8, 12, 56]

print()
#******************* Program 2 ***************************************
print('-'*15,"Program 2", '-'*15)
# Write a program to get all even and odd values with tags from the list
l1=[4,5,7,8,12]
l2=[]
for val in l1:
    if val%2==0:
        l2.append((val,'even'))
    else:
        l2.append((val,'odd'))
print("Result of odd and even value:",l2) # [(4, 'even'), (5, 'odd'), (7, 'odd'), (8, 'even'), (12, 'even')]

# solution with List comprehension

#if we have if and else both condition then for loop will come at last and then we need to write if else on left
result = [(x,'even') if x%2 == 0 else ('x','odd') for x in l1]
print("result :", result) # result : [(4, 'even'), ('x', 'odd'), ('x', 'odd'), (8, 'even'), (12, 'even')]

print()
#******************* Program 3 ***************************************
print('-'*15,"Program 3", '-'*15)
# get square of all values
l1=[5,7,8,2,9]

# solution with List comprehension
result=[x**2 for x in l1]
print(result)

#proper for loop
l2=[]
l3=0
for val in l1:
    l3=val**2
    l2.append(l3)
print("Square of each value:",l2) # Square of each value: [25, 49, 64, 4, 81]
