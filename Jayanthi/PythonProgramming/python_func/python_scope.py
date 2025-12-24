var_x=100
var_z=200
def add():
    global var_y
    var_y=200
    print("addition:", var_x+var_y)
add()

def mul():
    print("mul:", var_x * var_z)
    print("mul:",var_x * var_y) #error since no var_y in global
mul()

