# write a python program to get all the values which are divisible by 3 and 5 from set.

numbers = int(input( "enter a number:"))
if numbers % 3 == 0 and numbers % 5 == 0:
    print("Numbers divisible by 3 and 5:", numbers)
else:
    print("Numbers are not divisible by 3 and 5")

"""
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1
result_set = set()
for n in infinite_numbers():
    if n % 3 == 0 and n % 5 == 0:
        result_set.add(n)
    if len(result_set) == 10:
       break
print("Values divisible by 3 and 5:", result_set)
"""
