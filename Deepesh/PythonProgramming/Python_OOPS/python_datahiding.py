# Data Hiding in Python using Name Mangling
# In Python, data hiding is implemented using name mangling.
# Any attribute with a name starting with double underscores (__) is considered private
# Can not access directly from outside the class.

class DataHidingExample:

    def __init__(self, public_value, private_value):
        self.public_value = public_value          # Public attribute
        self.__private_value = private_value      # Private attribute

    def get_private_value(self, new_value):
        """Public method to access the private attribute."""
        self.protected_value = new_value # Protected attribute
        name = "Rahul"
        return self.__private_value
          

    def __set_private_value(self, value):
        """Public method to modify the private attribute."""
        self.__private_value = value
        print(self.public_value)

    def access_protected(self):
        """Public method to access the protected attribute."""
        print(self.protected_value)

    

# Creating an object of DataHidingExample

obj = DataHidingExample("I am public", "I am private")
print(obj.public_value)  # Accessing public attribute
#print(obj.__private_value)  # Attempting to access private attribute directly (will raise AttributeError)\

# access the private attribute using public method
print(obj.get_private_value())  # Accessing private attribute via public method

# access the private attrbute  using class name.
# obj._classname__attributename
print(obj._DataHidingExample__private_value)  # I am private
# Accessing private attribute using name mangling

# print(DataHidingExample.__private_value)
# AttributeError: type object 'DataHidingExample' has no attribute '__private_value'. Did you mean: 'get_private_value'?

# access the private method.
obj._DataHidingExample__set_private_value("New private value")
print(obj.get_private_value())  # Output: New private value


obj.access_protected()  # Accessing protected attribute via public method