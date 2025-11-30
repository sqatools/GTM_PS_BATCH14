#print values fron 1 to 10 using range loop
for i in range(1, 11):
    print(i)

#print value from 1 to 10 with step 2
for i in range(1, 10, 2):
    print(i)

#print value in reverse order from 10 to 1
for i in range(10, 0, -1):
    print(i)

print("_"*40)
#print value in reverse order till -5
for i in range(2, -6, -1):
    print(i)

print("_"*40)
# no output with range if values are not in range.
for i in range(10,1,1):
    print(i)

# default start value is 0 and default step is 1
print("_"*40)
for j in range(5):  # range(0, 5, 1)
    print(j)

print("_"*40)
# apply loop of different data types
list1=[5,7,8,2,5,18]
for val in list1:
    print(val)