# Create a dictionary based on the language of your choice with the numbers from 1-10 paired with the numbers
# from 1-10 in English. Create a quiz based on this dictionary. Display the number in a foreign language and
# ask for the number in English. Score the test and give the user a letter grade.

def main():
    count = 0
    print("Enter the number in English which corresponds to the number in French")
    num = {"un": "one", "deux": "two", 'trois': 'three', 'quatre': "four", 'cinq': 'five', 'six': 'six',
            'sept': 'seven', 'huit': 'eight', 'neuf': 'nine', 'dix': "ten"}

    for numbers in num:
        user = input("What is the equivalent of " + numbers + ": ")
        user = user.lower()
        if num[numbers] == user:
            print("Correct\n")
            count += 1
        else:
            print("Incorrect.The answer was " + num[numbers] + "\n")
    print("You got " + str(count))
    if count == 10 or count == 9:
        print("A")
    elif count == 8:
        print("B")
    elif count == 7:
        print("C")
    elif count == 6:
        print("D")
    else:
        print("F")


main()
