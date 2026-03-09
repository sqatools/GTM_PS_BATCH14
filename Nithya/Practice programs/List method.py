#Apply loop on list

a=['Apple','Banana','Carrot']

for looop in a:
    print(looop)
print("#"*50)

############################Slicing###############################
x=[1,2,3,4,5,6]
l=len(x)
for i in range(l):
    print(x)

print(x[0:3]) # 1 2 3 # excludes the last index position
print(x[-1:-2:-1]) #6
print(x[1:2])# 2,
print(x[0:len(x):2]) # 1,3,5
############################Methods#################################
#@@@@@@@@Append@@@@@@@@@

print(x.append(1)) # adds value to end of string
print(x)

#print(x.insert(10)[2]) # [1,2,10,3,4,5]
#print(x)

print("#"*50)
x=[189,20,3,4,90]
x.sort()
print(x) # sort doesnt store the value it only makes changes to original

x.sort(reverse = True) # reverse the ascending order
print(x)
x.reverse()
print(x)
y=[12,56,78,56,1]
y.count(12)
print(y.count(56))
y.clear() # clears everything in the variable
print(y)

a=[1,2,5,7]
b=[7,0,6,3]
c=a+b # concatenates values to new variable but no changes in original
print("a:",a , "b:",b,  "c:",c)

#  Q1 : write a python program to get all odd values from list
a=[21,44,7,90,14,43,57]
for o in a:
    if o%2!=0:
        print("Odd numbers:",o)
#using comprehension
 e= [x for x in a if x%2!== 0]
print("output:",e)









