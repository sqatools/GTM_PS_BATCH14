
print("conversion form int to float data type")
if1 = 100
if2 = float(if1)
print(if2)   # 100.0

print("*"*50)

print("conversion form float to intiger data type")

fi1 = 50.55
fi2 = int(fi1)
print(fi2)     #  50

print("*"*50)

print("conversion form float to complex data type")

fc1 = 30.55
fc2 = complex(fc1)
print(fc2)      # (30.55+0j)

print("*"*50)

"""
print("conversion form string to int data type")

si1 = "python"
si2 = int(si1)
print(si2)     --   #no value returned
"""

print("*"*50)
print("conversion form string to list data type")
sl1 = "python"
sl2 = list(sl1)
print(sl2)   # ['p', 'y', 't', 'h', 'o', 'n']

print("*"*50)
print("conversion form list to tuple data type")
lt1 = [10, 20, 30]
lt2 = tuple(lt1)
print(lt2)    # (10, 20, 30)

print("*"*50)
print("conversion form tuple to list data type")
tl1 = (10, 20, 30, 40)
tl2 = list(tl1)
print(tl2)   # [10, 20, 30, 40]

print("*"*50)
print("conversion form Dictionary to tuple data type")
td1 = {'a': 100, 123: "python",'b': 35+85J }
td2 = tuple(td1)
print(td2)   # ('a', 123, 'b')

print("*"*50)

"""
print("conversion form tuple to Dictionary data type")
dt1 = ('a', 123, 'b')
dt2 = dict(dt1)
print(dt2)   # no results 
"""

print("conversion form tuple to set data type")
ts1 = (10, 20, 30)
ts2 = set(ts1)
print(ts2)

print("*"*50)
print("conversion form set to tuple data type")
st_1 = {10, 20, 30}
st_2 = tuple(st_1)
print(st_2)

print("*"*50)