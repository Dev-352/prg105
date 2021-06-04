
number = 99
# loop to print the verses till i becomes 2
for i in range(number, 1, -1):
    print(str(i) + " bottles of beer on the wall, ")
    print(str(i) + " bottles of beer")
    print("Take one down, pass it around, " + str(i-1) + " bottles of beer on the wall...\n")

# the last two verses
if number >= 1:
    print("1 bottle of beer on the wall, ")
    print("1 bottle of beer")
    print("Take one down, pass it around, no more bottles of beer on the wall...\n")
