s = "Hello"
print(s)
print(dir(s))
##[ 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
# 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill']


list1 = [1,3,4,5,6]
print(list1)
print(dir(list1))
# [
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

tup = (1,2,4)
print(tup)
print(dir(tup))
#['count', 'index']


dict1 = {2:'a', 'a':5}
print(dict1)
print(dir(dict1))
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

st = {1,5,3,2}
print(st)
print(dir(st))
# ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

print("#"*50)
my_tuple = (1, 2, 3, 4, 5, 6)

subset = my_tuple[1:5]  # Slicing from index 1 to 5 (exclusive)
print(subset)  # Output: (2, 3, 4, 5)

subset = my_tuple[:3]  # Slicing from the start up to index 3 (exclusive)
print(subset)  # Output: (1, 2, 3)

subset = my_tuple[2:]  # Slicing from index 2 to the end
print(subset)  # Output: (3, 4, 5, 6)

subset = my_tuple[::2]  # Slicing with a step of 2
print(subset)  # Output: (1, 3, 5)