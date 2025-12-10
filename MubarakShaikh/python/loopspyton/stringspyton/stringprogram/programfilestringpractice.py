str6 = "Everything is possible with hard work"

# split the string into words
bond = str6.split()

largest = ""
second_largest = ""

for word in bond:
    if len(word) > len(largest):
        second_largest = largest
        largest = word
    else:
        if len(word) > len(second_largest) and word != largest:
            second_largest = word

print("second_largest:", second_largest)
