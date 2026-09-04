
# To call function defined in module1.py in module2.py we use from  and import keyword

from module1 import add # Here module1 is a file name and add is the name of function

# now use add function in this file

result=add(2,3)
print(result) #5

# To import all function defined in module1.py we use *

from module1 import *
result=greeting()
print(result) #Hello!


# If we import only module then we have to use function as module1.add
import module1
result=module1.add(5,6)
print(result)