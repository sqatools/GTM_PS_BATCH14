print("--"*50)
list1=[1,2,12.1,"nitin",True,[3,4,5,6]]
print(list1)
print(list1[2])

list2=[]
print("list2[]:",list2)
print(type(list2))

print("--"*50)
tup1=(1,2,3,4,5,6)
print(tup1)
tup2=()
print(tup2)
tup3=(1,2.01,"Hi",'nitin',[9,8,7],(3,4,5))
print(tup3)

print("--"*50)
dict={}
print(dict)
dict1={'a':1,'b':2,'c':3,'d':5}
print(dict1)
print(dict1['a'])
#dictionary with the key as immutable int,float,str,tuple
dict3={1:1201,1.1:35,'hi':'all',(1,2,3):'nitin'}
print(dict3)
print(dict3[(1,2,3)])

print("--"*50)
# set does not allow duplicate
set1=(1,'hi',2.3,(9,8,7),1)
print(set1)
set2=()
print(type(set2))