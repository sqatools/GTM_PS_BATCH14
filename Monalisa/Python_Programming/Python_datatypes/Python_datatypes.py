a=10
b=12.5
c=20+30j
print("a:", a, type(a))
print("b:", b, type(b))
print("c:", c, type(c))
print("Real number:",c.real)
print("IMG number:",c.imag)

s='monalisa'
s2=("monalisa is learning python"
    "in GTM")
s3=""" here i can add para
para can be of multiple lines
define para """

print(s)
print(s2)
print(s3)

s4="Monalisa"
print(s4[0])
print(s4[-8])
print(s4[(-2)**2])

#LIST- mutable, allows positive,negative , multi indexing

list1=[2,3,5+10j,'Hello',[3,6,9],(1,5,8),{7,90,98},True]
print("list", list1, type(list1))
print(list1[3][1])
print(list1[4][2])

tup1=(2,3,5+10j,'Hello',[3,6,9],(1,5,8),{7,90,98},True,"yesterday's")
print("list", list1, type(list1))
print(list1[3][1])
print(list1[4][2])


