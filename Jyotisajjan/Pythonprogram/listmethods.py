list1=[10,20,30,40,50,30]
print("list values:",list1)
##############################################
list1.append(40)
print("list1 values:",list1)
###########################################
list2=['Jyoti','sajjan']
#extend doest retrun the value
print(list2.extend(list1))
print(list2)
#####################################
list3={1,2,3,4,5}
list2.extend(list3)
print(list2)
###############################
list2.insert(1,'Kalyan')
print(list2)
##########################
list2.remove(30)
print(list2)
##########################
list2.pop()
print(list2)
list2.pop(1)
print(list2)
############################