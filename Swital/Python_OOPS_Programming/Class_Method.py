"""
# class method:
A method that is bound to the class and not the instance of the class.  
It takes 'cls' as the first parameter and can access class variables and other class methods.
"""
class Circle:
    # class variable
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius  # instance variable
    
    # class method
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
# creating an object of the Circle class using class method
a_obj = Circle.from_diameter(10)
print(f"Radius of circle with diameter 10: {a_obj.radius}")  # Output: Radius of circle with diameter 10: 5.0
