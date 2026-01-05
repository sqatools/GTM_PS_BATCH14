# Q1 python code to generate dictionary output from given string

str ="hello we are learning"
# output ={'H':'Hello
output={}
word_list=str.split(" ")
print(word_list)
for word in word_list:
    f_char=word[0]
    output[f_char]=word
print(output)

print('-'*50)
str1 ="hello we are learning"
# output ={'He':'Hello
output={}
word_list=str.split(" ")
print(word_list)
for word in word_list:
    f_char=word[0]+word[-1]
    output[f_char]=word
print(output)


# Q2 : write the python program calculate the bill as per the item purchase
dict_item={'Apple': 50, 'Banana':60, 'Mango':200, 'Watermelon':300}
item_purchase ={'Apple':5,'Banana':15,'Mango':5,'Watermelon':2}
total_bill=0
for fruit,prize in dict_item.items():
    print("Fruit Name:",fruit)
    print("Fruit Prize:",prize)
    print('fruit purchased',item_purchase[fruit])
    total_bill=total_bill+(prize*item_purchase[fruit])
    #print("fruit_bill",fruit_bill)
    #total_bill=total_bill+fruit_bill
print("Total bill:",total_bill)


#Q3 : 2). Python Dictionary program to print the square of all values in a dictionary.
"""Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64"""
print('-'*50)
input ={'a': 5, 'b':3, 'c': 6, 'd' : 8}
for i in input:
    print(i,":",input[i])

print('-'*50)
input ={'a': 5, 'b':3, 'c': 6, 'd' : 8}
for i in input:
    print(i,":",input[i])


#









