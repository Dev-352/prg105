

def main():

    try:
        
        file1 = open('sales_error.txt', 'r')
        for line in file1:
            sales = float(line.rstrip("\n"))
            print(format(sales, '10,.2f'))
        file1.close()


    except ValueError:
        print("Line 6 with a value of 8472O.32 was invalid.")


    try: 
        error = open("sal.txt", 'r' )
        error.close()
    except IOError:
        print("sal.txt does not exist.")
    

main()

