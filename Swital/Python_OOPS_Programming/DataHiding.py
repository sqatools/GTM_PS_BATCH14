# Data hiding in Python using Name Mangling - Encapsulation
# In Python, data hiding is implemented using name mangling.
# Any attribute with a name starting with double underscores (__) is considered private 
# and cannot be accessed directly from outside the class.

class DataHidingExample:

    def __init__(self, public_value, private_value):
        self.public_value = public_value          # Public attribute
        self.__private_value = private_value      # Private attribute

    def get_private_value(self):
        """Public method to access the private attribute."""
        return self.__private_value

    def __set_private_value(self, value):
        """Private method to modify the private attribute."""
        self.__private_value = value

    def access_private_method(self, value):
        """Public method to access the private method."""
        self.__set_private_value(value)
# Creating an object of DataHidingExample
obj = DataHidingExample("public", "private")
print(obj.public_value)  # Accessing public attribute
#print(obj.__private_value)  # Attempting to access private attribute directly (will raise AttributeError)
# Accessing the private attribute using public method
print(obj.get_private_value())  # Output: private
# Accessing the private attribute using name mangling
print(obj._DataHidingExample__private_value)  # Output: private
# Accessing the private method using name mangling
obj._DataHidingExample__set_private_value("new_private")
print(obj.get_private_value())  # Output: new_private
# Accessing the private method using public method
obj.access_private_method("another_private")
print(obj.get_private_value())  # Output: another_private

