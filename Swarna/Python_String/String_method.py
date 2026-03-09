print(dir(str))

# Upper() Lower() method
s1="Hello GooD MoRning"
print("Lower case result:",s1.lower())
print("Upper case result:",s1.upper())
# Isupper() and islower() method
s2="Python"
s3="PROGRAMMING"
s4="learning"

print(s2.isupper()) # False
print(s3.isupper()) # True
print(s4.islower()) # True
print(s2.islower()) # False

# swapcase() method
s5="Hello WORLD"
print(s5.swapcase()) # hELLO world

# title() method
s5="WE are leaRning PyThoN"
print("title output:",s5.title()) # We Are Learning Python
var=s5.title()
print("var:",var) # We Are Learning Python
print("s5:",s5) # WE are leaRning PyThoN

# capitalize() method
s6="wE are leaRning PyThoN"
print(s6.capitalize())

# count() method:
s7="wE areG leaRning PyThoN Programming"
print("count of g:",s7.count('g')) # 3
print("count of R:",s7.count('R')) # 1
print("count of ing:",s7.count('ing')) # 2

