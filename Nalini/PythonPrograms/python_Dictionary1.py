l1=['a','b','c']
l2=[10,20,30]
result= dict(zip(l1,l2))   # create a dictionary with ZIP function
print(result)
tup1=(10,2,5,6,7,8)


result2= tuple(x for x in tup1 if x%2==0)
print(result2)
# Python Dictionary program
# dictionary is mutable data type , we can update and modify
# key value pairs. last in first out concept.
dict1={'a':123,'b':'nalini',10:[2,3,4]}
print(dict1)

 # we cannot define the list as a key

print(dict1[b])
print(dict1[10][1])

dict2={'x':20,'y':30,'z':40}
for k,v in dict2.items():
    print(k,v)

# items is a method , we can get both key and value


#for k in enumarate(dict2):
   # print(k)

# this will get index
# add a data to dictionary
dict2['t']=60
# one data at a time
#update method---one dictionary dat to another
dict3= {'n':'nalini','age': 30, 'csass': 'mars'}
dict2.upate(dict3)



