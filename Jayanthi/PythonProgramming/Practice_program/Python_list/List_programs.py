# Q1 Write a python program to get all even value from list
# and store in list

list1=[4,5,7,8,12,17,56]
#output=[4,8,12,56]

output=[]

for i in list1:
    if i%2==0:
        output.append(i)
    else:
        continue
print("Output:",output)
print("*"*50)
# LIst comprehension

result=[x for x in list1 if x%2==0]
print(result)
print("*"*50)
# Q2 Write a python progrem to get all the even and odd value with tag from list

list2 =[4,5,6,7,8,12]
res=[]
for i in list1:
    if i%2==0:
        res.append((i,'even'))
    else:
        res.append((i,'odd'))
print(res)
print("*"*50)
# Comprehension
result1=[(i,'even') if i%2==0 else (i,'odd') for i in list2]
print(result1)

print("*"*50)
# get Square of all Value
List3= [5,6,7,8]
result2=[x**2 for x in List3]
print(result2)


