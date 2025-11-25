i1 = 4
i2 = 565
i3 = 54645645754745
print("i1 value", i1, type(i1))
print("i2 value", i2, type(i2))
print("i3 value", i3, type(i3))

# For float
f1 = 0
f2 = 6.4
f3 = 65.34244242425252
print("f1 value", f1, type(f1))
print("f2 value", f2, type(f2))
print("f3 value", i3, type(f3))

# Complex
c1 = 10 + 50j
print("c1 value", c1, type(c1))
print(c1.imag)
print(c1.real)

# String Datatype
s1 = "Hello"
print(s1)
s2 = """Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation. 
Python is dynamically type-checked and garbage-collected."""
print(s2)
# String Postive and negative number
st3 = "Programming"
print(st3[4])
print(st3[-5])
print(st3[8])
print(st3)

# list
print("____List Practise____"*5)
list1 = [2, 5.66, 4.5654333, 50 + 87j, [1, 4, 5], (3, 5, 3), {'v': 3121}, {12, 23, 131}, True]
print(list1[5])
print(list1[-7])
list2 = [54.423232323232, 5.66, "Hello World", 88 + 99j, [332.1, 435.32, 56.4], (5, 6, 6, 7, 6, 5, 3), {'a': "Data"},
         False, {12.323, 42, 3, 4}, True]
print(list2[7])
print(list2[-5])
list2.append(1001)
print("list2 :", list2)
print(list2, type(list2))

#Tuple
print("____Tuple Practise____"*5)
tup1 = (3, 15.66, 4, [1, 4, 5], (3, 5, 3), 50 + 87j, {'w': 123}, {12, 23, 131}, True)
print(tup1[3])
print(tup1[-4])
tup2 = (99, 0.567, 18, [8, 1], (3, 3, 3), 45+90j, {"name": "QA"}, {10, 20}, True)
print(tup2[6])

#Dictonary
print("Dictionary Practise____"*5)
dic1 = {"id": 1, "name": "Swital", "scores": [10, 20, 30], "active": True, "meta": {"age": 25}}
print(dic1["scores"])
dic2 = {"a":4, "class": "9th standard", "name": "serene"}
print(dic1["name"],"and", dic2["a"])
dic3 = {"a1":5, "des":54.65, "grade": "A"}
print(dic3["grade"])
dic4 = {
    200: "World",
    7.77: [10, 20, 30],
    12+4j: (1, 2),
    "xyz": {"p": 11, "q": 22},
    (4, 5): {100, 200, 100},
    False: 999
}
print(dic4, type(dic4))
print(dic4[0])

####Set
print("Set Practise____"*5)
s1 = {1, 2.5, 3+4j, True, (1, 2, 3), "hello"}
print(s1, type(s1))
s2= s2 = {10, 20.55, False, 9+2j, "QA", (5,)}
print(s2)
s3 = {100, "test", 4.44, (7, 8), 11+11j, True}
print(s3)
s4 = {5, 0.99, (3, 3, 3), "abc", 14+1j, False}
print(s4)