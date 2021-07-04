

def main():
    total = 0.0
    count = 0
    file = open("rainfall-totals.txt", "r")

    for line in file:
        line = line.rstrip("\n")
        rain = line.split()
        month = rain[0]
        amt = rain[1].split(".")

        if amt[0].isdigit() and amt[1].isdigit():
            amount = float(amt[0] + "." + amt[1])
            total = total + float(amount)
            count += 1
        else:
            print(month + " does not have a valid data because ")
            print(str(rain[1] + " is not a num"))
    file.close()
    avg = total / count
    print("The total rainfall for " + str(count) +
          " month is " + format(total, ',.2f'))
    print("The average rainfall was " + format(avg, ',.2f'))


main()
