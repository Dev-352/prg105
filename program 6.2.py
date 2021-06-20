
def main():
    file = open("sales_totals.txt", "r")
    total = 0
    count = 0
    avg = 0
    for line in file:
        sales = float(line.rstrip("\n"))
        print(format(sales, '10,.2f'))
        total += sales
        count += 1
    print("Total: " + format(total, '25,.2f'))
    print("Number of entries: " + format(count, '13,.0f'))
    avg = format((total/count), '23,.2f')
    print("Average: " + avg)
    file.close()


main()