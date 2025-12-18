# Diction is mutable
#LIFO


dict2={'x':22, 'y':33,'z':44}
for k,v in dict2.items():
    print("key",k,"value",v)
print('-'*50)
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

### Add data to dictonary ##

dict_a = {'a':125,'b':150}
dict_a['c']=200
print(dict_a)
# Update
print("-"*50)
dict_b={'d':'Name','p':200}
dict_c={'Name':'Jaya','Age':25}
dict_c.update(dict_b)
print(dict_c)

#Get
name_1=dict_c.get('Name')
print(name_1)

# Keys(),Values() these methods returns list od keys and values

print(dict_c.keys(),dict_c.values())

# Remove date using pop()
dict_d={'a':1,'b':2,'c':'e'}
val=dict_d.pop('a')
print(val)
print(dict_d)

# Popitem():remove Key value pair combination
print('-'*50)
dict_e={'a':1,'b':2,'c':'e'}
val1=dict_e.popitem()
print(val1)
print(dict_e)

# Clear: clear and only empty dictionary remain
print('-'*50)
dict_f={'a':1,'b':2,'c':'e'}
dict_f.clear()
print(dict_f)

# remove variable from memory using del
del dict_f
##print(dict_f)

# Copy dictionary shallow copy and deep copy
# Shallow copy: When one dict data is assigned to pther if we modify any of dictonary it will reflect in both dict

print('-'*50)
dict_i={'x':125,'y':150}
dict_j=dict_i
dict_j['z']=300
print(dict_i)
print(dict_j)

# Deep copy
print('-*50')
dict_k={'a':111,'b':222}
dict_l=dict_k.copy()
dict_l['c']=333
dict_k['d']=444
print(dict_k)
print(dict_l)

#Sorting
my_dict={'a':500,'e':200,'b':300,'c':700}
#sort with keys
sorted_dict= sorted(my_dict.items())
print(dict(sorted_dict))
#Sort with value
sorted_dict1=sorted(my_dict.items(),key=lambda item:item[1])
print(dict(sorted_dict1))










