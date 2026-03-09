str1 = "Hello we Are Learning Python"
# expected output1 = {'H': 'Hello', 'w': 'we', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

output = {}
word_list = str1.split(" ")
for word in word_list:
    f_char = word[0]
    output[f_char] = word

print(output)

print("#" * 50)
#######################################################################
# Home Work Python code to generate dictionary output from given string.

str2 = "Hello we Are Learning Python"
# expected output1 = {'Ho': 'Hello', 'we': 'we', 'Ae': 'Are', 'Lg': 'Learning', 'Pn': 'Python'}
result = {}
word_list1 = str2.split(" ")
for word in word_list1:
    f_char1 = word[0] + word[len(word) - 1]
    print(f_char1)
    result[f_char1] = word

print(result)

print("#" * 50)
#######################################################################
# calculate the bill as per the fruit items purchased.
price_dict = {'Apple': 50, 'Banana': 60, 'Mango': 200, 'watermelon': 300}
item_purchased = {'Apple': 5, 'Banana': 15, 'Mango': 5, 'watermelon': 2}
total_bill = 0
for fruit, price in price_dict.items():
    print("Fruit name: ", fruit)
    print("Price of fruit: ", price)
    print("Fruit details: ", item_purchased[fruit])
    fruit_purcharced = price * item_purchased[fruit]
    print("Fruit purchased: ", fruit_purcharced)
    total_bill = total_bill + fruit_purcharced
    print("Total bill is : ", total_bill)

####################Sorted Function#####################################
### sorted with keys in asecending order
dict_1 = {'a': 100, 'f': 120, 'c': 200, 'b': 300}
sorted_dict = sorted(dict_1.items())
print("Sorted with keys:", sorted_dict)

### sorted with values in asecending order
dict_1 = {'a': 100, 'f': 120, 'c': 200, 'b': 300}
sorted_dict1 = sorted(dict_1.items(), key=lambda a: a[1])
print("Sorted with values:", sorted_dict1)

### sorted with keys in decending order
dict_1 = {'a': 100, 'f': 120, 'c': 200, 'b': 300}
sorted_dict_desc = sorted(dict_1.items(), reverse=True)
print("Sorted with keys in descending order:", sorted_dict_desc)

### sorted with keys in decending order
dict_1 = {'a': 100, 'f': 120, 'c': 200, 'b': 300}
sorted_dict_desc1 = sorted(dict_1.items(), key=lambda a: a[1], reverse=True)
print("Sorted with values in descending order:", sorted_dict_desc1)

### sorted with keys in asecending order small and capital letter key
dict_1 = {'a': 100, 'F': 120, 'C': 200, 'b': 300}
sorted_dict = sorted(dict_1.items())
print("Sorted with keys:", sorted_dict)

### sorted with keys in asecending order small and capital letter key
dict_1 = {'A': 100, 'f': 120, 'c': 200, 'B': 300, 'a': 444}
sorted_dict = sorted(dict_1.items())
print("Sorted with small and capital letter key:", sorted_dict)

### sorted with keys in asecending order string values
dict_1 = {1: "Hi", 3: "data", 2: "For", 5: "Python", 4: "alpha"}
sorted_dict = sorted(dict_1.items())
print("Sorted with keys and string values:", sorted_dict)

### sorted with values in asecending order string values
dict_1 = {1: "Hi", 3: "data", 2: "For", 5: "Python", 4: "alpha"}
sorted_dict = sorted(dict_1.items(), key=lambda a:a[1])
print("Sorted with ascending order string values:", sorted_dict)
