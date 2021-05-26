# You are writing a program to sell tickets to the school play. If the person buying the tickets is a student,
# their price is $5.00 per ticket. If the person buying the tickets is a veteran, their price is $7.00 per ticket.
# If the person buying the ticket is a sponsor of the play, the price is $2.00 per ticket. If the person buying the
# ticket is a part of the general public, the price is $10.00.

# Displaying the public choice
print("PLAY PRICES PER TICKET")
print("1. Students $5.00")
print("2. Veteran $7.00")
print("3. Show Sponsor $2.00")
print("4. Retiree $6.00")
print("5. General Public $10.00")

# variables use to calculate
cal1 = 0
cal2 = 0
cal3 = 0
avg = 0

# asks user for how is buying and how much tickets the user want.
customer = int(input("Please enter the number of the category you fit for purchasing tickets: "))
num_tickets = int(input("How many tickets would you like to buy? "))

# using if-elif-else statement to get cost by the user input
if customer == 1:
    cal1 = num_tickets * 5.00
elif customer == 2:
    cal1 = num_tickets * 7.00
elif customer == 3:
    cal1 = num_tickets * 2.00
elif customer == 4:
    cal1 = num_tickets * 6.00
elif customer == 5:
    cal1 = num_tickets * 10.00
else:
    print("Invalid number entered.")

# prints the cost before applying any discount
print("Cost before any discounts were applied", format(cal1, '.2f'))

# calculating discount and average cost
if num_tickets > 15:
    cal2 = cal1 * 0.20
    cal3 = cal1 - cal2
    avg = cal3 / num_tickets
elif 15 >= num_tickets >= 9:
    cal2 = cal1 * 0.15
    cal3 = cal1 - cal2
    avg = cal3 / num_tickets
elif 8 >= num_tickets >= 4:
    cal2 = cal1 * 0.10
    cal3 = cal1 - cal2
    avg = cal3 / num_tickets
else:
    print("Sorry, you don't qualify for any discount")
#    print("your average ticket cost is: ", format(cal1 / num_tickets, '.2f'))

# if user wants less than 4 tickets this statement won't print
if num_tickets > 3:
    print("Your price after all discounts were applied is", format(cal3, '.2f'))
    print("Your price is", format(avg, '.2f') + " per tickets.")
