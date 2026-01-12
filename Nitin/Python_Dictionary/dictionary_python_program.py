#######################################################################
# Python code to generate dictionary output from given string.

str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

#empty dictionary varibale
dict1={}

#spliting a string into alist
list1=str1.split()
print(list1)
for word in list1: # Hello
    dict1[word[0]]=word
    print(dict1)


print("#"*50)
#######################################################################
#Home Work Python code to generate dictionary output from given string.
str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}
dict2={}
list2=str2.split()  #Hello we Are
for word in list2:
    dict2[word[0]+word[1]]=word
    print(dict2)


print("#"*50)
#######################################################################
# calculate the bill as per the fruit items purchased.
price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}


fruit_bill_dict={}
for fruit,price in price_dict.items():

    #get fruit name
    print("Fruit Name:",fruit)

    #get fruit price
    print("Fruit Price:" ,price)

    # get fruit purchased
    print("fruit purchased :", item_purchased[fruit])
    print("*"*20)
    # get fruit bill
    fruit_bill = price * item_purchased[fruit]
    fruit_bill_dict[fruit] = fruit_bill
    print("Fruit bill :", fruit_bill)

print("#"*50)
#######################################################################
'''
2). Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
'''
dict3={'a':5,'b':3,'c':6}
