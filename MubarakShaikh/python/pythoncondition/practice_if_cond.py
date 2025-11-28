num1 = input("Please enter your value:")
# input accepts the values in string format only
print(num1, type(num1))
x = int(num1)

if x % 3 == 0 and x % 5 == 0:
    print("This number is divisible by 3 and 5 :", x)
else:
    print("This number is not divisible by 3 and 5 :", x)


    ######################
    marks = int(input("Please enter your marks:"))

    if marks <= 30:
        print("Failed in Exam")
    elif 30 < marks <= 40:  # chain action logic
        print("Pass with 3rd grade")
    elif marks > 40 and marks <= 60:
        print("Pass with 2nd grade")
    elif marks > 60 and marks <= 80:
        print("Pass with 1st Grade")
    elif marks > 80 and marks <= 100:
        print("Pass with A++ Grade")
    else:
        print("Marks should be less than 100")
##########################################
print("_" * 50)

val = int(input("plz input value:"))
list1 = [5, 7, 9, 2, 50, 6]

if val in list1:
    print("number is available in the list:", val)
else:
    print("number is not available in the list", val)
##########################################
print("_" * 50)

dict1 = {'a': 123, 'b': 456, 'c': 678}
val1 = 'a'

if val1 in dict1:
    print("this val1 key is available in dict")
    print(dict1[val1], val1)
else:
    print("this val1 key is not available in dict")
