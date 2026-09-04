# Datatype Conversion
num = 10
var = float(num)
print(var, type(var))

# float -> int
var2 = 23.56
var3 = int(var2)
print(var3, type(var3))

print("_"*50)
## string -> int ###
s1 = "1234"
p1 = int(s1)
print(p1, type(p1), p1*2)
print("_"*50)

## string -> list ###
str2 = "PythonnPh"
l1 = list(str2)
print(l1, type(l1))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>

t1 = tuple(str2)
print(t1, type(t1))
# ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'>

# convert string to set
set1 = set(str2)
print(set1, type(set1))
# {'h', 'P', 't', 'n', 'y', 'o'} <class 'set'>

###### list #########
# print("_"*50)
# list -> set
list1 = [2, 3, 5, 6, 8, 7, 9, 8]
set2 = set(list1)
print(set2, type(set2))

print("_"*50)
# set - list
set3 = {4, 6, 8, 8, 1, 3, 7, 7}
l2 = list(set3)



