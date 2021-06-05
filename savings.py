# Write a program that projects yearly income, the amount saved towards retirement each year,
# and total retirement savings. Assume a 3 percent raise on the starting income each year,
# and a 6% yearly return on investment. You will need to ask the user their current age,
# at what age they want to retire, what their current income is, what percent of their income they save each year,
# and how much they currently have in savings. You will calculate how many years until retirement,
# and display the projected income, savings contribution, and total savings each year.

# Inputting user info
current_age = int(input("How old are you currently? "))
retire_age = int(input("At what age do you want to retire? "))
income = int(input("What is your yearly income? "))
savings_percent = int(input("What percent of your income do you save? "))
total_savings = int(input("How much money do you currently have in savings? "))

# calculating before entering loop
contribution = income * (savings_percent / 100)
# 6% rate of return
total_savings = total_savings * 1.06
# money added in the year
total_savings += contribution
cal_age = retire_age - current_age
# print(cal_age)
print("Year", "         Income", "          Saving Contribution", "          Total Savings")
for i in range(1, cal_age + 1):
    print(format(i, '3'), format(income, '16,.0f'), format(contribution, '27,.0f'), format(total_savings, '25,.0f'))
    income = income * 1.03
    contribution = income * (savings_percent / 100)
    total_savings = total_savings * 1.06
    total_savings += contribution
