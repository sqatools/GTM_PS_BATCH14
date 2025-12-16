str1 = "hello we are learning python"

words = str1.split()
letter_dict = {word[0] + word[-1]:
 word for word in words if len(word) >= 2}

print("\nUsing dictionary comprehension:")
print(letter_dict)