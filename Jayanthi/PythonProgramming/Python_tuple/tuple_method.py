tup2=(10,20,30,50)
for val in tup2:
    print(val)

"""Count and index only the method"""
(print('*'*50))
# Count
print(tup2.count(20))
print(tup2.index(30))

# repeat
print(tup2*2)

# Concat
tup3=tup2+tup2
print(tup3)

# Max and MIn
tup6=(8,9,10,23,56)
print("Max:",max(tup6))
print("min:",min(tup6))
print("sum:",sum(tup6))

# Program to get combination of numbers whose sum is 10
print('*'*50)
tup6=(5,7,8,2,3,1,9)
# output=[(7,3),(8,2),
output=[]
for i in range(len(tup6)):
    for j in range(len(tup6)-1):
        if tup6[i]+tup6[j]==10:
         output.append((tup6[i],tup6[j]))
        else:
            continue
print("output:",output)

# Write a python program to create a dictionary with zip function using lists

print('*'*50)
l1=[8,9,'python']
l2=[7,7,'fun']
r1=dict(zip(l1,l2))
print(r1)


