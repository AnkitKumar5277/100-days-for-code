# Python Program to Display Powers of 2 Using Anonymous Function
# Display the powers of 2 using anonymous function
# terms = 10
# Uncomment code below to take input from the user
terms = int(input("How many terms? "))
# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
# # output
# The total terms are: 10
# 2 raised to power 0 is 1
# 2 raised to power 1 is 2
# 2 raised to power 2 is 4
# 2 raised to power 3 is 8
# 2 raised to power 4 is 16
# 2 raised to power 5 is 32
# 2 raised to power 6 is 64
# 2 raised to power 7 is 128
# 2 raised to power 8 is 256
# 2 raised to power 9 is 512

