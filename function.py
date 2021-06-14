# Write a program that asks a user to enter a whole number between 20 and 100.
# Send that number to a function that will validate the number, and if it is not a number between 20 and 100,
# use a while loop to keep asking the user for a valid number. Return the number to the main function
# (hint good_number = validate(num) - use a variable to store the returned value).


def main():
    num = int(input("enter number between 20 to 100: "))
    if 100 >= num >= 20:
        two(num)
        three(num)
        five(num)

    else:
        print("Enter valid number")


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
