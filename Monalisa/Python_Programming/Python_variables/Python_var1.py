a1=10
print ("value of a is" , a1, id(a1))
# id gives u memory location of variable
b1=100
print ("value of b is" , b1, id(b1))

##assign diff value to different var at a time##
p1,q1,r1= 2.2,32.4,5.67777
print ("value of p is" , p1)
print ("value of q is" , q1)
print ("value of r is" , r1)

##math operations
print ("div with single /", q1/r1)#get entire integer with decimal values
print ("div with double//", q1//r1)#get only whole number
print ("multiplication product", q1*r1)
print( "addition", q1+r1)
print( "subtraction", q1-r1)

#power operator **
print ("sq of number ", a1**2)
print ("cube  of number ", a1**3)
print ("quad  of number ", a1**4)

#remainder  operator %
print ("remainer  of number ", r1%p1)

#compare   operator ( == or !=)
print (a1==b1)
print (a1!=b1)
#repeat printing  - 50 times
print("-"*50)
print("Hello zz  "*5)

#python is case sensitive
name= "Mona"
Name= "lisa"
NAME= "puja"
print(name,"!",Name,"!",NAME,"@@@")