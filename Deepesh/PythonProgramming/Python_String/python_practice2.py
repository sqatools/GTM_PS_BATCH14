str1 = input("enter a string : ") # Hello we are LeArning PythOn

word_list = str1.split(" ")
print(word_list) # ['hello', 'we', 'are', 'learning', 'python']
print("total words :", len(word_list)) # total words : 5

max_len = 0
largest_word = ""

for word in word_list: # 
    print(word) # hello, we, are, learning, python
    if len(word) > max_len: # 5 > 0, 2 > 5, 3 > 5, 8 > 5, 6 > 8
        max_len = len(word) # 5, 8
        largest_word = word # hello, learning
    else:
        continue


print("largetst word :", largest_word)
print("longest word length :", max_len)

