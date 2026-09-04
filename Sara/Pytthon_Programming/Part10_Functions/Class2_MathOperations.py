# pass by valued

def addition(n1, n2):
    print(f"Addition of {n1}, {n2}:", n1 + n2)
addition(30, 50)

"""
********OUTPUT********

PS C:\PythonAutomationProject\GTM_PS_BATCH14\Sara\Pytthon_Programming\Part10_Functions> python Class2_Program
.py 
Addition of 30, 50: 80
"""
#############################################################

# Pass by Reference

def substraction(e,f):
    print(f"Substraction of {e},{f}:", e-f)

num1=20
print("-" * 50)
num2=5
substraction(num1, num2) # Substraction of 20,5: 15

print("-" * 50)
###########################################################
# Adding a list and dictionary

def list_dict(a,b):
    print(f"List and dict addition of {a}, {b}:", a + b)

l1=[10,20,30]
dict1={'a':2,'b':4}
# list_dict(l1, dict1) 
#TypeError: can only concatenate list (not "dict") to list

###########################################################
# Adding list
def list1(a,b):
    print(f"List and dict addition of {a}, {b}:", a + b)

l1=[10,20,30]
l2=[40,50,60]
list1(l1, l2)
"""
^********OUTPUT********
List and dict addition of [10, 20, 30], [40, 50, 60]: [10, 20, 30, 40, 50, 60]
"""
print("-" * 50)
###########################################################
