# You will be tracking the number of steps someone takes each day for a week. Using a loop,
# ask them to enter the date and the number of steps. At the end of the program,
# you will display the total number of steps taken, the day with the most steps, and the day with the least steps.
# Print multiple days if they are tied.


def main():

    days = {}
    total = 0
    max = 0
    min = 5000000000000
    print("You will be entering the data and the number of step taken for each days in week.")
    for day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
        steps = int(input("Please enter the umber of steps taken on " + day + ": "))
        days[day] = steps
        if steps > max:
            max = steps
        if steps < min:
            min = steps
        total = total + steps
    avg = total/7
    print("you walked a total of " + format(total, ',.0f') + " steps during the week.")
    print("That was an average of " + format(avg, ',.0f'))
    print("The maximum steps you took were: " + str(max) + " on ")
    for i in days:
        if days[i] == max:
            print(i)
    print("The minimum steps you took were: " + str(min) + " on ")
    for i in days:
        if days[i] == min:
            print(i)


main()
