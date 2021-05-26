# You are writing a program to determine if a student is eligible for financial aid for the next semester. To qualify,
# the student must either be a new student, or a current student with a GPA of 2.0 or higher.  Additionally,
# the student may not have a criminal record for drugs, must enroll in a minimum of six credit hours of classes,
# and must have a gross yearly income of less than $50,000.  You will gather information from the student,
# and you will let them know if they are eligible for financial aid or not.

# using a boolean
eligible_for_financial_aid = True

student_status = input("Are you a new or returning student. Please enter n or r: ")

# gpa = float(input("What is your GPA? "))
# calculating process if the user meets the requirements or not
if student_status == "n":
    eligible_for_financial_aid = True
elif student_status == "r":
    gpa = float(input("What is your current GPA? "))
else:
    eligible_for_financial_aid = False

# checking  criminal record
criminal_record = input("Have you ever been convicted of a drug felony? (enter y or n) ")
if criminal_record == "y":
    eligible_for_financial_aid = False

# checking credit hours
credit_hours = int(input("How many credit hours are you enrolled for next semester? "))
if credit_hours < 6:
    eligible_for_financial_aid = False

# checking yearly income
gross_yearly_income = float(input("What is your gross yearly income, round to the nearest dollar? Don't use commas. "))
if gross_yearly_income >= 50000:
    eligible_for_financial_aid = False

if eligible_for_financial_aid:
    print("Yes, you are eligible for financial aid")
if not eligible_for_financial_aid:
    print("No, you are not eligible for financial aid.")
