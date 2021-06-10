# Create a program that presents the user with five choices. The topic could be game characters, food, car packages,
# anything you are interested in. You will put a menu on the screen, ask the user to enter the number or letter
# of their choice, and then call the corresponding function to give the user more information.

# printing options

def main():
    print("Select one of the menu options below to find out more")
    print("A. Monte Cristo")
    print("B. Ruben")
    print("C. Submarine")
    print("D. Grilled Cheese")
    print("E. Gyro")
    letter = input("Please enter the letter of your choice")

# checks what letter is entered and if invalid letter is entered it will not take it
    if letter == "A":
        monte_cristo()
    elif letter == "B":
        ruben()
    elif letter == "C":
        submarine()
    elif letter == "D":
        grilled_cheese()
    elif letter == "E":
        gyro()
    else:
        print("Enter valid letter")

# defines all letter fuctions


def monte_cristo():
    print("Fresh monte cristo sandwich")
    print("Served with a side of hot tomato soup.")


def ruben():
    print("Fresh ruben sandwich")
    print("Served with a side of hot tomato soup.")


def submarine():
    print("Fresh submarine sandwich")
    print("Served with a side of hot tomato soup.")


def grilled_cheese():
    print("Fresh grilled cheese sandwich")
    print("Served with a side of hot tomato soup.")


def gyro():
    print("Fresh gyro sandwich")
    print("Served with a side of hot tomato soup.")
