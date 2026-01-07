def addition(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Both inputs must be numbers."
    
output = addition(5,'a')  
print(output)  # Output: Error: Both inputs must be numbers.


"Multiple Exceptions"

def multiple(a,b):
    try:
        print("Multiplication of values are:", a,b)
        result = a * b
        except TypeError:
            return "Error: Both inputs must be numbers."
        except Exception as e:
            return f"An unexpected error occurred: {e}"


Result= multiple(2,"Test")
print(Result)
    
