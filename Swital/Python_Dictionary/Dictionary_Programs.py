str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

output = {}
word_list = str1.split(" ")
for word in word_list:
    f_char = word[0]
    output[f_char] = word

print(output)

print("#"*50)
#######################################################################
#Home Work Python code to generate dictionary output from given string.

str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}
result = {}
word_list1 = str2.split(" ")
for word in word_list1:
    f_char1 = word[0] + word[len(word)-1]
    print(f_char1)
    result[f_char1] = word

print(result)

print("#"*50)
#######################################################################
# calculate the bill as per the fruit items purchased.
price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}
total_bill = 0
for fruit, price in price_dict.items():
    print("Fruit name: ", fruit)
    print("Price of fruit: ", price)
    print("Fruit details: ", item_purchased[fruit])
    fruit_purcharced = price*item_purchased[fruit]
    print("Fruit purchased: ", fruit_purcharced)
    total_bill = total_bill + fruit_purcharced
    print("Total bill is : ", total_bill)