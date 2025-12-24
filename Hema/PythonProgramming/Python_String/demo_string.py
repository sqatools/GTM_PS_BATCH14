name = "Python Programming Language"
print("Length of string:", len(name))  # 27
print("Index of P:", name.index("P"))  # 0
print("Index of g:", name.index("g"))  # 16 (first occurrence)
print("Count of a:", name.count("a"))  # 3


count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
print("Final count:", count)  # 6