def addition(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Both inputs must be numbers."
    
addition(5,'a')   
