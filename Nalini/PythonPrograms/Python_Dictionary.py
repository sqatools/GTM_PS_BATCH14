# tuple is a immutable data type, we cannot modify.
# we can define with round brackets
tup1=(1,3,5,"Nalini",[20,30,50])
print(tup1,tye(tup1))
print (tup1[::-1])
# reverse a tuple
tup2=(10,20,50)
for val in tup2:
    print(val)

print(dir(tuple))
# methods----count and index methods
tup3 = (a,b,c,5,10,a,b,t,y)
print("count of a:",tup3.count('a'))
print ("index of 5:",tup3.index(5))

tup4=tup3+(10,20,30)
#concat both
print(tup4)
print("max value",max(tup4))
print("min value",min(tup4))
print("sum value",sum(tup4))
# these are inbuilt functions

# get combination of numbers whose sum is 10.
tup5=(7,3,5,8,2,5,9,1)
#output=[(7,3),(9,1),(8,2),(5,5)]
output=[]
for i in range(len(tup5)):
    for j in range(len(tup5)):
        if tup5[i]+tup[j]==10:
            output.append((tup[i],tup5[j]))
        else:
            continue
print(output)

# we can use tuple when data is fixed  like months in a year, days  etc

