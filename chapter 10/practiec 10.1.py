# Design a class that holds the following personal data: name, address, age, and phone number.
# Write appropriate accessor and mutator methods (get and set). Write a program that creates three
# instances of the class. One instance should hold your information and the other two should hold your friends'
# or family members' information.  Just add information, don't get it from the user.  Print the data from each object,
# make sure to format the output for clarity and ease of reading.

class Person_data:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone= phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return 'Name: ' + self.__name + "\nAddress " + self.__address + "\nAge: " + self.__age + "\nPhone: " + \
               self.__phone


def main():
    person1 = Person_data("Meri", "123 Disney Land, Florida", "15", "815-234-3221")
    person2 = Person_data("Tammy", "234 Hapsburg dr, Atlanta", "20", "224-444-4444")
    person3 = Person_data("Jason", "Camp Crystal lake", "71", "N/A")

    print(person1)
    print("------------------------------")
    print(person2)
    print("------------------------------")
    print(person3)


main()
