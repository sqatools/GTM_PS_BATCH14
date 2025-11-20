# Variable declaration
x = 20
# x : variable
# = : assignment operator
# 15 : value

print(x, id(x))
y = 25
z = 35
print("value of x :", x)  # 20
print("value of y :", y)  # 25
print("value of z :", z)  # 35
w = 15
print("value of w :", w, id(w))
print("value of w :", w, id(w))

#### Assign one single value to multiple variables ###
a1 = b1 = c1 = 100
print("value of a1 :", a1)
print("value of b1 :", b1)
print("value of c1 :", c1)
## Assign different values in one line ##
t1, t2, t3 = 100, 200, 300
print("value of t1 :", t1)
print("value of t2 :", t2)
print("value of t3 :", t3)
print("_" * 50)

### Math operations ###
num1 = 8
num2 = 3

v=num1+num2
print("addition :", num1 + num2)       # 11
print("subtraction :", num1 - num2)   # 5
print("multiplication :", num1 * num2)   # 24
print("division / :", num1 / num2)       # 2.6666
print("addition of value :", v) #2.3333
print("division with single /:", num2/3)  # 6.666666
print("division with double //:", num2//3) # 6
print("subtraction :", num1-num2)

print("_" * 50)
# comparison operators
n1 = 40
n2 = 50
n3 = 40
print(n1 == n2) # False
print(n1 == n3) # True
print(n1 != n2) # True
# Repeat a string
print(" Python "*4)

print("_" * 50)
val1 = 900
val2 = 1000
print(val1, val2)
print(val1, end=" ")
print(val2, end=" ")

print()
print("_" * 50)

### Rules For Variable Names###
# 1. No spaces in name
# user age = 20   (invalid)
user_age = 20    # valid
# 2. No length limit
python_is_easy_to_learn = True
# 3. Cannot start with number
# 9data = 100  (invalid)
data9 = 100     # valid
# 4. Only underscore allowed as special character
# data@value = 500  (invalid)
data_value = 500 # valid
# 5. Variable names are case-sensitive
student = "Amit"
Student = "Sumit"
STUDENT = "Rohan"
print(student, "|", Student, "|", STUDENT)
print("_"*50)