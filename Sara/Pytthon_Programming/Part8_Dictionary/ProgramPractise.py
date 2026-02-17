print("*"*15,'Program 1', "*"*15)
print(" Python code to generate dictionary output from given string.")

str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

result1={}
word_list=str1.split(" ")
print(word_list) # ['Hello', 'we', 'Are', 'Learning', 'Python']
for i in word_list:
    f_word=i[0]
    result1[f_word]= i
print('result1 :', result1) # result1 : {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

print()
###################################################################
print("*"*15,'Program 2', "*"*15)
#Home Work Python code to
print(" Generate dictionary output from given string. ")

str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}
result2={}
word_l=str2.split(" ")
# print(word_l)

for i in word_l:
    for j in i:
        f_w2=j[-1]
    f_w1 = i[0]
    s1=f_w1+f_w2

    result2[s1]=i
print('Result 2:', result2)
# Result 2: {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}

print()
###################################################################
print("*"*15,'Program 3', "*"*15)
print("Calculate the bill as per the fruit items purchased. ")

price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}
total_bill=0
fruit_price={}

for i, j in price_dict.items():
    print('fruit name:', i)
    print('fruit price:', j)
    print('total price of per fruit', item_purchased[i])
    fruit_bill= j * item_purchased[i]
    print('total of per fruits is: ', fruit_bill )
    total_bill = total_bill + (j * item_purchased[i])
    print('-' * 15)
print('Total Bill of all itens is:', total_bill) # Total Bill of all itens is: 2750

print()
###################################################################
print()
###################################################################
print("*"*15,'Program 4', "*"*15)
print("Calculate the bill as per the fruit items purchased. ")

price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}
total_bill=0
fruit_price={}

for i, j in price_dict.items():
    print('fruit name:', i)
    print('fruit price:', j)
    print('total price of per fruit', item_purchased[i])
    fruit_bill= j * item_purchased[i]
    print('total of per fruits is: ', fruit_bill )
    total_bill = total_bill + (j * item_purchased[i])
    print('-' * 15)
print('Total Bill of all itens is:', total_bill) # Total Bill of all itens is: 2750


fruit_bill_dict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5':'five',
                   '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
word_result = ""
for val in str(total_bill):
    print(val)
    word_result = word_result + fruit_bill_dict[val] + " "

print("bill on words :", word_result)

print("Fruit bill data :", fruit_bill_dict)
# Fruit bill data : {'Apple': 250, 'Banana': 900, 'Mango': 1000, 'watermelon': 600}



