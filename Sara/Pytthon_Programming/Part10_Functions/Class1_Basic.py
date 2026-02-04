def addition():
    global var_p, var_x
    var_x = 300
    var_p = 100
    var_y = 500 # local variable
    print("var_x :", var_x)
    print("addition :", var_x + var_y)

addition()