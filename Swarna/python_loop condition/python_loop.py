'''for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i,end=" ")

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

for i in range(6):
    print(i*"*")
    for i in range(4,-1,-1):
        print(i*"*")'''

for i in range(10, 1, -1):
    if i == 5:
        break
    print(i)

print("_"*40)

for i in range(10): # i = 0
    if i == 3 or  i == 5 or i == 7:
        continue # police man
    print(i)