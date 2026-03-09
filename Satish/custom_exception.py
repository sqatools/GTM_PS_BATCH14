
class Myclass(Exception):
    """Learning Custom Exception"""
    pass

def divide(a,b):
    try:
        if b == 0:
            raise Myclass("Can not divide by Zero")
        print(a/b)
    #except Exception as e:
    except Myclass as e:
        print("In except block:",e)


divide(10,0)

