for i in range(1,10,1):
    print(i,end=" ")
print()
print(" i values are:", end=" ")

for i in range(1,10,2):
    print(i,end=" ")

print()
# not in range
for i in range (10,1):
    print(i)
print()

print("i values are:",end=" ")
for i in range (10,1,-1):
    print(i,end=" ")
print()
list=[1,2,3,4,5,6,7,78]
for num in list:
    if(num%2)==0:
        print("even numbers:",num)


