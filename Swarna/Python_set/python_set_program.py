# write a python program to get all the values which are divisible by 3 and 5 from set.

numbers = {10, 15, 33, 45, 60, 22, 90, 120, 37}
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print("Numbers divisible by 3 and 5:", num)
    else:
        print("Numbers are not divisible by 3 and 5")
