################################
list1=(2,4,6,8,9,0)
for i in range(-1,-len(list1)-1,-2):
    print(list1[i])
################################
print("#"*50)
list1=(5,8,9,10,50)
for val in list1:
    if val%2 == 0:
        print(val,end=" ")

#############################
print("#"*50)
for i in range (1,4,6):
    print("address :i", i)
    for j in range(2,4,1):
        print("package : j", j)
############################################
for i in range(1, 6, 1): # i = 1, 2, 3, 4, 5
    print("Address : i=",i)
    # package : inner loop
    for j in range(1, 4, 1): # j = 1, 2, 3
        print("Package : j=", j)

    print("_"*20)
###########################Find numbers divisible by a certain number
for i in range(1500,2701):
    if i%5==0 and i%7==0:
        print(i)

print("_"*40)
##################################

