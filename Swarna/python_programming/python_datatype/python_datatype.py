# Integer data type
n1 = 0
n2 = 1
n3 = 876546789344
n4 = 989898987657676765
n5 = 78.89
print("n1 :", n1, type(n1))
print("n2:",n2, type(n2))
print("n3:", n3, type(n3))
print("n4:", n4, type(n4))
print("n5:", n5, type(n5))
print("_"*50)

# float data type
var1=0.0
var2=5.6
var3=7896.65436788
print("var1:", var1, type(var1))
print("var2:", var2, type(var2))
print("var3:", var3, type(var3))
print("_"*50)

#complex data type
p1 = 10+20j
print("p1:",p1, type(p1))
print("real number:",p1.real)
print("img number:",p1.imag)
p2=40+50j
print(p2)

print("_"*50)

#Sequential data type
s1=""
s2='Hello'
s3="H"
print("s1:", s1, type(s1))
print("_"*15)
print("s2:", s2, type(s2))
print("_"*15)
print("s3:", s3, type(s3))

abc="Hello"
abc="python"
print(abc)

# String follows positive negative indexing
str10="Python"

print(str10[0])
print(str10[-4])
#print(str10[-7])#error
print(str10[-2 ** 2])
print(str10[(-2)** 2])# apply BODMAS rule
print("_"*50)

#########List###########
list1=[2,3.7,3+30j,'Hello',[3,4,5,],(1,5,7),{'a':123},{5,7,8},True]
print(list1,type(list1))#[2, 3.7, (3+30j), 'Hello', [3, 4, 5], (1, 5, 7), {'a': 123}, {8, 5, 7}, True] <class 'list'>

print(list1,type(list1))

list2=[4,7,5,8,63]
print(list2[2])#5
print(list2[-2])#8

print("_"*50)
list3=[2,3.7,3+30j,'Hello',[3,5,6],(1,5,7),{'a':123},{5,7,8},True]
print(list3[4])#[3,5,6]
print(list3[4][1])#5

print(list3[2])#3+30j
print(list3.index(True))#8

list4=[6,8,9]
list4.append(100)
print("list4:",list4)
#list4:[6,8,9,100]

print("_"*50)

##############Tuple###########
tup1=(2,3.5,2+3j,'python',[3,6,8],(1,4,7),{'a':456},{4,7,8},False,"Yesterday's")
print(tup1, type(tup1))