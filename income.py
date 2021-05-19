# The program should get input from the user and convert each of the inputs to floats.
# The program should tell the user how much money they have left after it subtracts the budgeted items from the income.
# The program should calculate and display the income percentage of each budget item.

# getting users data
monthly_income = float(input("What is you total net monthly income? "))
housing = float(input("How much do you spend on housing each month? "))
food = float(input("How much do you spend on food each month? "))
transportation = float((input("How much do you spend on transportation each month? ")))
phone = float((input("How much do you spend on your phone bill each month? ")))
utilities = float((input("How much do you spend on your utilities each month? ")))
clothing = float((input("How much do you spend on clothing each month? ")))

# calculations
housing_per = housing / monthly_income
food_per = food / monthly_income
transportation_per = transportation / monthly_income
phone_per = phone / monthly_income
utilities_per = utilities / monthly_income
clothing_per = clothing / monthly_income

total_left = monthly_income - (housing + food + transportation + phone + utilities + clothing)
print("\nHousing takes up " + format(housing_per, ',.2%') + " of your monthly budget")
print("Food takes up " + format(food_per, ',.2%') + " of your monthly budget")
print("Transportation takes up " + format(transportation_per, ',.2%') + " of your monthly budget")
print("Phone bill takes up " + format(phone_per, ',.2%') + " of your monthly budget")
print("Utilities take up " + format(utilities_per, ',.2%') + " of your monthly budget")
print("Clothing takes up " + format(clothing_per, ',.2%') + " of your monthly budget")
print("\nYou have $" + format(total_left, ',.2f') + " left from your income after paying these monthly expenses")
