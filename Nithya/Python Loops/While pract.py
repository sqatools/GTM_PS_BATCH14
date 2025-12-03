print("X"*20,"02-12-2025","X"*20 )
print("\t \t \t \t While Loop")

# print values from 1 to 10 using while loop
i=0
while i <= 10:
    print(i)
    i=i+1
    print("X"*20)

# get all the even number from 1 to 20

for i in range(1,21):
    if i%2==0:
        print(i)
    else:
        continue
print("X"*30)
# skip values 5,10 from 1 to 10 with continue statement
a=1
while a <= 10:
    if a%5==0:
       a+=1
       continue
    else:
        print(a)
        a += 1

print("X"*30)
# break statement practice
for Count in range (1,10):
    print(Count)
    if Count==5:
        print("Match found", Count)
        break
else:
    print("No match found",Count)

print("X"*30)










