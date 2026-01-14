#######################################################################
# Python code to generate dictionary output from given string.

str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

# empty dict variable
output1 = {}
# split to get list of words
word_list = str1.split(" ") # ['Hello', 'we', 'Are', 'Learning', 'Python']
print(word_list)

for word in word_list: # Hello
    f_char = word[0]  # H
    output1[f_char] = word  # H: Hello
    print(output1)

print("output1 :", output1)



print("#"*50)
#######################################################################
#Home Work str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}

print("*"*50)
output1 = {}
word_list = str1.split(" ")
str1 = "Hello we Are Learning Python"
# empty dict variable
output1 = {}
# split to get list of words
word_list = str1.split(" ") # ['Hello', 'we', 'Are', 'Learning', 'Python']
print(word_list)

for word in word_list: # Hello
    f_char = word[0]
    f_char1 = word[-1]
    f_char2 = f_char+f_char1
    output1[f_char2] = word

print("output1 :", output1)






print("#"*50)
#######################################################################
# calculate the bill as per the fruit items purchased.
price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}

fruit_bill_dict = {}
total_bill = 0
for fruit, price in price_dict.items():
    # get fruit name
    print("fruit_name :", fruit)
    # get fruit price
    print("fruit_price :", price)
    # get fruit purchased
    print("fruit purchased :", item_purchased[fruit])
    # get fruit bill
    fruit_bill  = price * item_purchased[fruit]
    fruit_bill_dict[fruit] = fruit_bill
    print("Fruit bill :", fruit_bill)
    # get total bill
    total_bill = total_bill + fruit_bill

    print("_"*20)

print("Total fruit bill :", total_bill) # Total fruit bill : 2750
print("Fruit bill data :", fruit_bill_dict)
# Fruit bill data : {'Apple': 250, 'Banana': 900, 'Mango': 1000, 'watermelon': 600}


print("#"*50)
#######################################################################
# calculate the bill as per the fruit items purchased.
price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}

total_bill = 0
for fruit, price in price_dict.items():
    # get fruit name
    print("fruit_name :", fruit)
    # get fruit price
    print("fruit_price :", price)
    # get fruit purchased
    print("fruit purchased :", item_purchased[fruit])
    # get fruit bill
    fruit_bill  = price * item_purchased[fruit]
    fruit_bill_dict[fruit] = fruit_bill
    print("Fruit bill :", fruit_bill)
    # get total bill
    total_bill = total_bill + fruit_bill

    print("_"*20)

print("Total fruit bill :", total_bill) # Total fruit bill : 2750

fruit_bill_dict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5':'five',
                   '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
word_result = ""
for val in str(total_bill):
    print(val)
    word_result = word_result + fruit_bill_dict[val] + " "

print("bill on words :", word_result)

print("Fruit bill data :", fruit_bill_dict)
# Fruit bill data : {'Apple': 250, 'Banana': 900, 'Mango': 1000, 'watermelon': 600}