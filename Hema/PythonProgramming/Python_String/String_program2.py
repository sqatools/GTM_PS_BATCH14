# Q6 :  write a python Program to get second-largest word from given string.
str6 = "Everything is possible withingourlimit hard work"
output = "possible"

word_list = str6.split(" ")
print(word_list)
largst_word = ""
sLargest_word= ""

for word in word_list: # Everything, is possible withingourlimit
    if len(word) > len(largst_word):
        sLargest_word  = largst_word # "" # Everything
        largst_word = word # Everything, withingourlimit

    elif len(word) > len(sLargest_word) and len(word) < len(largst_word):
        sLargest_word = word # is, possible

print("Largest word :", largst_word)
print("second Largest word :", sLargest_word)

