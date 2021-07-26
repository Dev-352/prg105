import tkinter


class MilesPerGallonCalculator:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Creating main frame with name name main_frame
        self.main_frame = tkinter.Frame()

        # Inserting title for frame
        self.title_frame = tkinter.Frame(self.main_frame)
        self.title_label = tkinter.Label(self.title_frame)
        self.title_label.pack()
        self.title_frame.pack()

        # Input 1 for number of gallons
        self.gallon_frame = tkinter.Frame(self.main_frame)
        self.gallon_label = tkinter.Label(self.gallon_frame, wraplength=300, width=50,
                                          text="Enter how many gallons your cars holds:"
                                          )
        self.gallon_entry_val = tkinter.StringVar()
        self.gallon_entry = tkinter.Entry(self.gallon_frame, width=10, textvariable=self.gallon_entry_val)
        self.gallon_label2 = tkinter.Label(self.gallon_frame, width=7, justify="left")
        self.gallon_label.pack(side="left")
        self.gallon_entry.pack(side="left")
        self.gallon_label2.pack(side="left")
        self.gallon_frame.pack()

        # Input 2 for number of miles same code as input 1 with change in variable names.
        self.miles_frame = tkinter.Frame(self.main_frame)
        self.miles_label = tkinter.Label(self.miles_frame, wraplength=300, width=50,
                                         text="How many miles have you traveled:")
        self.miles_entry_val = tkinter.StringVar()
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10, textvariable=self.miles_entry_val)
        self.miles_label2 = tkinter.Label(self.miles_frame,  width=7, justify="left")
        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")
        self.miles_label2.pack(side="left")
        self.miles_frame.pack()

        # Calculate button
        self.button_frame = tkinter.Frame(self.main_frame)
        self.calculate_button = tkinter.Button(self.button_frame, text="Convert",
                                               command=self.calculate_mileage)

        self.calculate_button.pack(side="left")
        self.button_frame.pack()

        # Output
        self.results_frame = tkinter.Frame(self.main_frame)
        self.results_label_val = tkinter.StringVar()
        self.results_label = tkinter.Label(self.results_frame, textvariable=self.results_label_val)
        self.results_label.pack()
        self.results_frame.pack()
        self.main_frame.pack()
        tkinter.mainloop()

    def calculate_mileage(self):
        try:
            miles = float(self.miles_entry_val.get())
            gallons = float(self.gallon_entry_val.get())
            mileage = miles / gallons
            self.results_label_val.set("Converted to miles per gallons: {:.2f} ".format(mileage))
        except ValueError:
            self.results_label_val.set("Incorrect input given. Try again.")


result = MilesPerGallonCalculator()
