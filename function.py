# Write a program that asks a user to enter a whole number between 20 and 100.
# Send that number to a function that will validate the number, and if it is not a number between 20 and 100,
# use a while loop to keep asking the user for a valid number. Return the number to the main function
# (hint good_number = validate(num) - use a variable to store the returned value).


def main():
    num = int(input("Enter number between 20 to 100: "))
    valid(num)
    two(num)
    three(num)
    five(num)


def valid(num):
    if 100 >= num >= 20:
        return num
    else:
        while num < 20 or num > 100:
            print("Not valid number")
            num = int(input("Enter number between 20 to 100: "))
    return num


def two(num):
    if (num % 2) == 0:
        print(str(num) + " is divisible by 2")
    else:
        print(str(num) + " is not divisible by 2")


def three(num):
    if (num % 3) == 0:
        print(str(num) + " is divisible by 3")
    else:
        print(str(num) + " is not divisible by 3")


def five(num):
    if (num % 5) == 0:
        print(str(num) + " is divisible by 5")
    else:
        print(str(num) + " is not divisible by 5")


main()
