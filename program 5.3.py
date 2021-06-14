def main():

    # print("This program will find the area of shape for you. ")
    # print("1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit")
    # num = int(input("Please enter the number of your selection: "))
    # valid(num)
    menu = 0
    while menu <= 5:
        print("This program will find the area of shape for you. ")
        print("1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit")
        menu = int(input("Please enter the number of your selection: "))
        valid(menu)
        if menu > 4:
            print("Goodbye")
            break
        elif menu > 3:
            circle()

        elif menu > 2:
            square()

        elif menu > 1:
            triangle()

        else:
            rectangle()


def valid(num):
    if num <= 5:
        return num
    else:
        while num > 5:
            print("This is not a valid number")
            print("This program will find the area of shape for you. ")
            print("1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit")
            num = int(input("Please enter the number of your selection: "))
    return num


def rectangle():
    width = float(input("Enter the width of the rectangle in cm: "))
    height = float(input("Enter the height of the rectangle in cm: "))
    area = width * height
    print("The are of the rectangle is ", format(area, ',.2f') + " square cm")


def triangle():
    base = float(input("Enter the base of the triangle in cm: "))
    height = float(input("Enter the height of the triangle in cm: "))
    area = (base * height) / 2
    print("The are of the triangle is ", format(area, ',.2f') + " square cm")


def square():
    length = float(input("Please enter the length of one side of the square: "))
    area = length * length
    print("The area of the square is ", format(area, ',.2f') + " square cm")


def circle():
    radius = float(input("Please enter the length of the radius of the circle: "))
    PI = 3.14
    area = PI * (radius * radius)
    print("The area of the circle is ", format(area, ',.2f') + " square cm")


main()
