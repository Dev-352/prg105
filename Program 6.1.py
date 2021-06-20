# Write a program that gathers contact information from people.
#  The program should ask the user how many entries they are going to make, 
# then ask for the Name, phone number, and email address for each person.
# You will be writing this information to a file. Separate each value with a comma,
# and make sure to include the new line symbol.


def main():
    num_file = int(input("How many people do you want to add to the file? "))
    #count = 0
    contact_info = open("contact.txt", "w")
    for count in range(1, num_file + 1):
        name = input("What is the name of the person? ")
        phone_num = input("What is their phone number? ")
        email = input("What is their email address? ")
        contact_info.write(name + ", " + phone_num + ", " + email + "\n" )

    contact_info.close()


main()