num = 11
count=0

for i in range(2,num):
    if num%i==0:
        count=count+1
        print(i)
        break
    else:
        continue

if count>0:
    print("This is not prime")
else:
    print("This is  prime")

print("---"*10)

