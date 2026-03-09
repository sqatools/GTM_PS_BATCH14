str_p = "Learning Makes Success"
str_p1 = "THE"
str_p2 = "Data"
str_p3 = "learn"
result1 = str_p.upper()
print("Upper method:", result1)
result2 = str_p.lower()
print("Lower method:", result2)
result3 = str_p1.isupper()
print("Is upper method:", result3)
result4 = str_p2.isupper()
print("Is upper method:", result4)
result5 = str_p3.isupper()
print("Is upper method:", result5)
result6 = str_p3.islower()
print("Is lower method:", result6)
result7 = str_p1.islower()
print("Is lower method:", result7)
result8 = str_p.capitalize()
print("Capitalize method:", result8)
result9 = str_p.swapcase()
print("SwapCase method:", result9)
result10 = str_p.count("e")
print("Count method:", result10)
result11 = str_p.count("Makes")
print("Count method:", result11)
result12 = str_p.index("a")
print("Index method:", result12)
result13 = str_p.title().find("Makes")
print("Find method:", result13)
result14 = str_p.find("is")
print("Find method:", result14)
result15 = str_p.replace("Makes", "Make")
print("Replace method:", result15)
# Using partition() to split a string based on the first occurrence of a substring
my_string = "Hello world! Welcome to Python."

# Split the string at the first occurrence of ","
result = my_string.partition("!")

print(result)

# Example using expandtabs() to replace tabs with spaces
text = "Hello\tWorld\tPython"
expanded_text = text.expandtabs(5)  # Replaces tabs with 4 spaces

print(expanded_text)