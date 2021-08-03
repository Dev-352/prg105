# In this program I have made a Bank App where User can deposit, withdraw and check balance.

from tkinter import *
from tkinter import messagebox

root = Tk()


class Bank:

    # default constructor of Bank class
    def __init__(self):
        self.balance = 0
        # label for amount
        self.l1 = Label(root, text="Enter Amount : ")
        self.l1.grid(row=0, column=0)
        # textbox for entering amount
        self.t1 = Entry(root)
        self.t1.grid(row=0, column=1)
        # Buttons for check balance , withdraw , deposit
        check = Button(root, text="CheckBalance", command=self.checkBalance)
        withdraw = Button(root, text="Withdraw", command=self.withdraw)
        deposit = Button(root, text="Deposit", command=self.deposit)
        # placing the buttons in a grid layout
        check.grid(row=1, column=0)
        withdraw.grid(row=1, column=1)
        deposit.grid(row=1, column=2)

    # method for check balance
    def checkBalance(self):
        messagebox.showinfo("Balance", "Balance : " + str(self.balance))

    # method for withdraw
    def withdraw(self):
        amt = int(self.t1.get())
        # if the entered amount is greater than current balance we report an error
        if self.balance < amt:
            messagebox.showerror("Error", "Low Balance \n" + "Your current balance: " + str(self.balance))
        else:
            # withdrawing amount
            messagebox.showinfo("Message", "Withdrawal of " + str(amt) + " successful")
            self.balance -= amt

    # method to deposit amount
    def deposit(self):
        amt = int(self.t1.get())
        self.balance += amt
        messagebox.showinfo("Message", "Deposit of " + str(amt) + " successful")


App = Bank()
root.mainloop()
