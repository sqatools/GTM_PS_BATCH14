# 1). Python program to calculate the square of each number from the given list.
l1 = [1,3,4,5,8]
for a in l1:
    print("Square of", a, ":", a**2)

# 2). Python program to combine two lists.
l2 = [2,3,5,6,1]
l2p = [7,8,9]
print("Combine two list:", l2+l2p)

# 3). Python program to calculate the sum of all elements from a list.
l3 = [3,6,2,8,7]
print("Summation is:", sum(l3))

# 4). Python program to find a product of all elements from a given list.
l4 = [1,4,2,3,5]
var = 1
for val in l4:
    var *= val
print("Product of all elements:", var)

# 5). Python program to find the minimum and maximum elements from the list.
l5 = [3,2,5,3,6]
print("Maximum number is:", max(l5))
print("Minimum number is:", min(l5))

# 6). Python program to differentiate even and odd elements from the given list.
l6 = [3,4,2,5,6,8]
odd = []
even = []
for val in l6:
    if val%2 == 0:
        even.append(val)
    else:
        odd.append(val)
print("Even numbers list:", even)
print("Odd numbers list:", odd)

# 7). Python program to remove all duplicate elements from the list.
l7 = [3,2,4,5,2,5,3,2,6,7,1]
list = []
for val in l7:
    if val not in list:
        list.append(val)
print(list)

# 8). Python program to print a combination of 2 elements from the list whose sum is 10.
l8 = [4,7,5,3,5,2,8,5]
total = []
for i in range(len(l8)):
    for j in range(i+1, len(l8)):
        if l8[i]+l8[j] == 10 and (l8[i], l8[j]) not in total and (l8[j], l8[i]) not in total:
            total.append((l8[i], l8[j]))
            
print(total)

l8 = [4,7,5,3,5,2,8,5]
seen = set()
pairs = []

for num in l8:
    diff = 10 - num
    if diff in seen:
        pairs.append((diff, num))
    seen.add(num)

print(pairs)

# 9). Python program to print squares of all even numbers in a list.
l9 = [4,5,2,7,6,9]
for val in l9:
    if val%2 == 0:
        print(f"{val} is even and its square is:", val**2)

# 10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
#Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
#Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]

l10 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
even = []
odd = []
for val in l10:
    if val %2 == 0:
        even.append(val)
    else:
        odd.append(val)
odd.extend(even)
print(odd)