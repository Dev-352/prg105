"""
    Write a GUI program that displays your name and address when a button is clicked (you can use the address of the
     school). The program’s window should resemble the sketch on the far left side of figure 13-26 when it runs.
     When the user clicks the Show Info button, the program should display your name and address as shown
     in the sketch on the right of the figure
"""
import tkinter


class MyGUI:

    def __int__(self):
        self.main_window = tkinter.Tk()

        # Creating a StringVar to display
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # creating two frames
        self.info = tkinter.Frame(self.main_window)
        self.button = tkinter.Frame(self.main_window)

        # creating a label widgets
        self.name_label = tkinter.Label(self.info, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info, textvariable=self.csz_value)

        # packing the labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # creating button widgets
        self.show_info = tkinter.Button(self.button, text="Show Info", command=self.show)
        self.quit = tkinter.Button(self.button, text="Quit", command=self.main_window.destroy)

        self.show_info.pack(side="left")
        self.quit.pack(side="right")

        self.info.pack()
        self.button.pack()

        tkinter.mainloop()

    def show(self):
        self.name_value.set("Dev Patel")
        self.street_value.set("123 Mchenry Ave")
        self.csz_value.set("Mchenry, IL 60001")


my_gui = MyGUI()
