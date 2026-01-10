from class_C import C
class D(C):
    def method_d(self):
        return "Method D from class D"
    

obj = D()

print(obj.method_a())  # Inherited from class A
print(obj.method_b())  # Inherited from class B       
print(obj.method_c()) # Inherited from class C
print(obj.method_d())  # Method from class D