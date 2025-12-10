str6 = "Everything is possible with hardinigddf work"
word_list = str6.split(" ")
largest_word = ""
slargst_word = ""

for word in word_list:
    #print(word, len(word))
    word_len = len(word)
    if word_len > len(largest_word):
        slargst_word = largest_word
        largest_word = word
    elif word_len > len(slargst_word) and word != largest_word:
        slargst_word = word
    else:
        continue

print("second Largest word:", slargst_word, largest_word   )




