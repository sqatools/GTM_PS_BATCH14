######################## Data_types #################

""""
1. Number
     i) Integer
    ii) Float
   iii) complex

2. Sequencial:
      i) string
     ii) list
    iii) tuple

3. Dictionary
4. set
5. Boolean
"""


################################## Int ##################################

i = 100
i1 = 1000000000001
i2 = 20202020151502156201
i3 = 484516548548440084801
i4 = 55457777148121212121215151556549845225121865515623186
i5 = 654845615846515815645646545649848945645616512151561654545484565545
print(i, type(i))
print(i1, type(i1))
print(i2, type(i2))
print(i3, type(i3))
print(i4)
print(i5)

print("*"*50)
############################ Float ###############################

f1 = 100.1532
f2 = 29.5
f3 = 3.330
f4 = 5645654546545645646545.184854651845489485454654545465456454
f5 = 4650.6545
print(f1, type(f1))
print(f2, type(f2))
print(f3, type(f3))
print(f4, type(f4))
print(f5)

print("*"*50)

########## complex ########

c  = 10j+30
c1 = 20+50j
c2 = 500+60j
print (c, type(c))
print (c1, type(c1))

print("*"*50)

########################### String ###########################

s1 = 'python'
s2 = "programming"
s3 = " python programming 'language' "
s4 = ' python programming "language" '
#s5 = 'python programming 'language''
#s6 = "python programming "language""
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4)

print("*"*50)

s7 = """
Python is a versatile, high-level, 
and easy-to-learn programming language known for
its clear syntax that emphasizes readability. 
It is used for a wide variety of tasks, including web development,
data science, automation, and software development. 
Python is dynamically typed and interpreted, meaning code 
is executed line by line and variables don't require 
explicit type declarations. 
"""
print(s7, type(s7))

print("*"*50)

s8 = "sathish"
"""
0   1  2  3  4  5  6
s   a  t  h  i  s  h 
-7 -6 -5 -4 -3 -2 -1
"""
print(s8[6])
print(s8[-1])

print("*"*50)

################################## list ################################

list = [123, 33.65, 50+45j, [1, 2, 3, 4],(9, 8, 7, 6, 5, 4), {13: "python"},{4, 5, 6, 2}, True]
print(list, type(list))
print(list[3][0])

list2 = ["P", 20, 35, 25]
print(list2[3])
print(list2[-4])

list3 = [100, 200, 300]
list3.append(400)  # adding another value in the list using "append"
print(list3)

print("*"*50)

############################## tuple #########################

tup = (123, 33.65, 50+45j, [1, 2, 3, 4],(9, 8, 7, 6, 5, 4), {13: "python"},{4, 5, 6, 2}, True)
print(tup[3])

tup1 = (100, 200, 300)
#tup1.append(400)
print(tup1)


print("*"*50)

########################### Dictionary ########################

dict = {'a':100, "b": 200, 123: "python"}
print(dict)

dict['c']=300  # adding another key with value
print(dict)

print("*"*50)

dict1 = {100: '14',
         10.5: [1, 2, 3],
         1+12j: {"a": 100},
         'python': (14, 15, 16),
      #  [10, 20]: {100, 200, 300}, unhashable type: 'list'. we can not list as a key
         (30, 40): "programing",
         "abc": 100
         }

print(dict1)

print("*"*50)

########################### set ########################

set1 = {10, 20.28, 20+36j,'programing', (500, 600, 800), True, False}
print(set1)


print("*"*50)
####################### Boolean ###########################

b1 = 100
b2 = 200
b3 = 100
b4 = 205
print(b1==b3)
print(b2==b1)
print(b3==b4)
print(b4==b2)

print("*"*50)