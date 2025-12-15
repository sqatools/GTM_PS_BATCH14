#print(" if conditions ")

if_1 = 100
if_2 = 200
if_3 = 300
if_4 = 100

if if_1 == if_4:
    print("if_1 and if_4 values are matching:", if_1, if_4)
else:
    print("if_1 and if_4 values are not matching:", if_1, if_4)

print("_"*50)

if_5 = 100
if_6 = 200
if_7 = 300
if_8 = 100

if if_6 == if_7:
    print("if_6 and if_7 valus are matching:", if_6, if_7)
else:
    print("if_6 and if_7 values are not matching:", if_6, if_7)

print("_"*50)


#print(" if and elif and else conditions ")

a = 10
b = 20
c = 30
d = 40
e = 10

if a == b:
    print("a is matching with b", a , b)
elif a == c:
    print("a is matching with c", a ,c)
elif a == d:
    print("a is matching with d", a, d)
elif a == e:
    print("a is matching with e", a , e)
else:
    print("a is not matching with any value")

print("_"*50)



# nested if conditions

batch1 = "cleared"
batch2 = "cleared"
batch3 = "cleared"

if batch1 == "cleared":
    print("you cleared 1st round of exam")


    if batch2 == "cleared":
        print("you cleared 2nd round of exam")


        if batch3 == "cleared":
            print("you cleared 3rd round of exam")


        else:
            print("you have not cleared 3rd round of exam better luck next time")


    else:
        print("you have not cleared 2nd round of exam better luck next time")


else:
    print("you have not cleared 1st round of exam better luck next time")







