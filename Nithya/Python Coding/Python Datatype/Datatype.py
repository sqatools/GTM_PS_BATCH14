print("*" *20, "Datatype","*" *20)

a=10
b=2.2
c="All are String"
d= "This is also a string"
e='Single quote is a string we can write 10000 line al;so on a single line' \
  'it will work in new line too'
Square="2**2"
print("output of a", a,type(a))
print("output of b", b,type(b))
print("output of c", c,type(c))
print("output of d", d,type(d))
print("output of e", e,type(e))
print("output of square:", Square,type(Square))
print ("a+b=c", a,"+",b,"=",c)

print('*'*100)
print ("Day 2 - Datatype continuation")

Student1=[11,"Nithy",'5.1m']
Student2=[9002,'Divya',9952577]
Student3=['Govt Entrance', "18-Apr-20",True]
Student4=["2+2j,(2,5,7)"]

print(Student1,Student3)
Student4.append("Im New")
print(Student4)
print("_Tuple_"*10)

Tuple1=("Try",356,[1,5,8],2+5j,False)
Tuple2=({'apple':780}, '12-11-2025')
Tuple3=({19,679,658}, (738,698), )
Tuple4= ('training on python' , "9:00-10:00 PM")
print(Tuple1,"\n", Tuple2)

print(" Dictionary "*10)

Grocery={'Nuts':250 , 'Furits':500 , 'Veggies': 250}
Phase1={'[A,B,C]':'Alphabets'}
Phase2={(1,2,3):'Number'}
print("Grocery",Grocery)
print(Phase1,Phase2)

print(" Set "*10)
Set1={1,'Hi'}
Set2={'Testing',False}
Set3={1,3,3,"testing",'testing'}
print(Set3)

print(" Boolean "*10)

Building=5000
Land=206877
Discount=201877
print(Building!=Land)
print((Discount+Building)==Land)

