# Datatype Conversion

# int -> float
num = 30
var = float(num)
print(var, type(var))  # 30.0 <class 'float'>

# float -> int
var2 = 45.56
var3 = int(var2)
print(var3, type(var3))  # 45 <class 'int'>

print("_"*50)
## string -> int ###
s1 = "5678"
p1 = int(s1)
print(p1, type(p1), p1*2)
# 5678 <class 'int'> 11356


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

############ list #########
# print("_"*50)
# list -> set
list1 = [5, 7, 9, 5, 2, 5, 7, 8]
set2 = set(list1)
print(set2, type(set2))
# {2, 5, 7, 8, 9} <class 'set'>


print("_"*50)
# set - list
set3 = {6, 8, 3, 8, 2, 3, 5, 7}
l2 = list(set3)
print(l2)  # [2, 3, 5, 6, 7, 8]