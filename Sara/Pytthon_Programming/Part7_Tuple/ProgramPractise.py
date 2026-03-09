# program to get combination of number whose sum is 10
t1 = (5, 7, 8, 2, 3, 1, 9)
result=[]

for i in range (len(t1)):
    for j in range (i+1,len(t1)):
        if t1[i]+ t1[j]==10:
            result.append((t1[i],t1[j]))
        else:
            continue
print("Results: ",result) # Results:  [(7, 3), (8, 2), (1, 9)]

print('*'*50)
##########################################################

# program to get all even numbers/values from tuple
t2= (3,4,2,6,5,7,8)
r1=tuple(x for x in t2 if x%2==0)
print('Even values: ', r1) # Even values:  (4, 2, 6, 8)


