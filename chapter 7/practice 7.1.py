# Ask the user how many students are in their class. Get the student's name and final grade. 
# Store the answers in a two-dimensional list, then write the list to the grades.txt file. 


def main():
    # setting line and s_grades to null string
    line = []
    s_grades = []
    # getting integer input of number of student
    num_students = int(input("How many students do you need to enter grades for? "))
    # using for loop to enter info of every student
    for student in range(0, num_students):
        # getting name of student and adding student + 1
        name = input("Enter the name of the student " + str(student + 1) + ": ")
        grade = input("Enter the student's final letter grade: ")
        line.append(name)
        line.append(grade)
        s_grades.append(line)
        line = []
    print(s_grades)

# using method provided
    outfile = open("grades.txt", 'w')
    for line in s_grades:
        lineo = "'" + line[0] + "', '" + line[1] + "'\n"
        outfile.writelines(lineo)
    outfile.close()


main()
