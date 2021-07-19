import officeFurniture
import Desk


def main():
    # create a Furniture object
    chair = officeFurniture("chair", "leather", "5", "9", "12", "450")
    # create a Desk object
    desk = Desk("cedar", 10, 20, 15, 250, "right", 12)
    # display the chair and desk
    print(chair)
    print(desk)


main()
