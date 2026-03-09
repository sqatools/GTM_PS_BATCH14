#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).#Input1:1500#Input2:2700
for i in range(1500, 2700):
    if i % 7 ==0 and i % 5 ==0:
        print(i)
print("_"*20)
#########################
"""3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python” """
word = input(" Enter your word : ")
word2 = " "
for i in str(word):
    word2 = word2 + i
print(" Output will be : ", word2)