# Static Method in Python OOPS Programming
"""
# Static methods are methods that belong to the class rather than any specific instance.
# They do not require a reference to 'self' or 'cls' and cannot access instance or class variables directly.
# They are defined using the @staticmethod decorator.
# Static methods are used for utility functions that are related to the class but do not need to
# access any class or instance-specific data.
"""
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def greet():
        return "Hello, welcome to Math Operations!"
# Using static methods without creating an instance of the class
sum_result = MathOperations.add(10, 20)
product_result = MathOperations.multiply(5, 4)
greeting = MathOperations.greet()
print(f"Sum: {sum_result}")            # Output: Sum: 30
print(f"Product: {product_result}")    # Output: Product: 20
print(greeting)                       # Output: Hello, welcome to Math Operations!
