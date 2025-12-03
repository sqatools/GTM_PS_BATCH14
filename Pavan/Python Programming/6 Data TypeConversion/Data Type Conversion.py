# Datatype Conversion#
###int --> Float###
num = 40
var =float(num)
print(var ,type(var))

###Float to Int ###
print("*"*50)
var2 =99.9
var3=int(var2)
print(var3 ,type(var3))
print(var2 ,type(var2))
print("*"*50)

###String to Int ###
s9 ="1909"
print(s9,type(s9))
s10 =int(s9 )
print(s10 ,type(s10))
print("*"*50)
s5 = 55
s6 =str(s5)
print(s6,type(s5))

print("*"*50)
###string to List ###
a = "python"
b=list(a)
print(b ,type(b))
print("*"*50)
###Tupple ###
t1 =tuple(a)
print(t1 ,type(t1))
###Set##
s1 =set(a)
print(s1 ,type(s1))

###list to Set  ####
List1 =[1,3,4,9,0,4,9,48,4]
set1= set(List1)
print(set1 ,type(List1))
####set to List###

set1 =(1,2,23,3,33,4,3,4,2,)
L1 =list(set1)
print(L1,type(L1))


