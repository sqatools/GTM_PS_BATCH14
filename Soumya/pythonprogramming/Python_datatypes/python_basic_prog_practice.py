a = 10
b = 20
c = 30
a = 40
print(a, type(a)) # 40
print(b, type(b)) # 20
print(c, type(c)) # 30
d = 112123232, 67.7
print(d, type(d))

#####################################float

print("#"*30)
e =5.9
f =56789876.987
print(e, type(e))
print(f, type(f))

######################################complex
#####################################syntax ------x+yj
print("#"*30)
g = 4+6j
print(g, type(g))
print("real number :", g.real)
print("imaginary number :", g.imag)


############################################String
print("-"*100)
str1 = ""
s2 ="hello"
s3 ='hi'
s4 = """dfghjkkjhghj
fghjklkjhg
04"""
s5 = "dfghjklkjh'g"
s3 = "hi01"
print(str1, type(str1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))
print(s3[1])
print(s3[-1])
print(s3[-2+1])
print(s3[0:2])
print(s3[-1-2])

######################################list
print("#"*30)
l1 = [1, 2.5, "hell", 2+6J, [1,3,5], (3,5), 1 , {a : "hi"}, {1, 7},True]
print(l1, type(l1))
print(l1[-1])
l1.append("hi")
print(l1)
print(l1[-1])
print(l1[-3])
l1.insert(0, "test")
print(l1)
print(l1[-1])
l1.reverse()
print(l1)
l1.pop(3)
print(l1)

####################################tuple
print("#"*30)
t1 = (1, 3, 4, 7 , 1, "hi")
print(t1, type(t1))
print(t1[-1])
print(t1[4])


#########################dictionary
print("#"*30)
dict = {a:"hi", 1:5, (1, 5):6, a:500}
print(dict)
print(dict[a])
dict[b] = 4
print(dict)

#########################################set
print("#"*30)
set111 = {2, 4, 2, 2, "hi", 'hello', 2+5J}
print(set111)

##################################################boolean
print("#"*30)
i = 10
k = 20
l= 20
print(i==k)
print(k==l)









