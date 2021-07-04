#  Check to see if the data is valid, if it is not valid, indicate to the user what the bad data is.
#  Total and average the data, and display formatted results on the screen.


def main():
    # setting integers to 0
    total = 0.0
    count = 0
    # opening file
    file = open("rainfall-totals.txt", "r")
    # Using for loop to strip \n and split after space and '.'
    for line in file:
        line = line.rstrip("\n")
        rain = line.split()
        month = rain[0]
        amt = rain[1].split(".")
        # if the amt is digits it will continue else it will through error
        if amt[0].isdigit() and amt[1].isdigit():
            amount = float(amt[0] + "." + amt[1])
            total = total + float(amount)
            count += 1
        else:
            print(month + " does not have a valid data because ")
            print(str(rain[1] + " is not a num"))
    # closing file
    file.close()
    # calculating the avg
    avg = total / count
    # print output
    print("The total rainfall for " + str(count) +
          " months is " + format(total, ',.2f'))
    print("The average rainfall was " + format(avg, ',.2f'))


main()
