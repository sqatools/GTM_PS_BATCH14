def add(a,b,c=6,d=2):
    print(f'Add of {a},{b},{c},{d}:', a+b+c+d)

add(2,3) # Add of 2,3,6,2: 13

print("-"*30)
'''
def add(a,b=2,c,d=2):
    print(f'Add of {a},{b},{c},{d}:', a+b+c+d)

add(2,3)  # SyntaxError: parameter without a default follows parameter with a default

'''

