# import specific function or variable from another module
# from module1 import addition, greeting

# import everything from module1 to module2
# from module1 import *

# import module and name with short name
from module1 import multiplication as abc

"""
r1 = addition(40, 50)
print("Result :", r1)

print(greeting)

r2 = multiplication(5, 6)
print("result mul :", r2)
"""

r3 = abc(6, 7)
print("multiplication output :", r3)