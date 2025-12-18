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


