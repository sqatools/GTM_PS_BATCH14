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