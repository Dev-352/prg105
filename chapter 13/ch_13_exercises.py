"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)


# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text="Hello World!!")
        self.label.pack()
        tkinter.mainloop()


# my_gui = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2


# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # Creating two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # label widgets
        self.label1 = tkinter.Label(self.top_frame, text="Dev Patel")
        self.label2 = tkinter.Label(self.top_frame, text="Computer Science")

        # adding the labels to the top frame
        self.label1.pack(side="top")
        self.label2.pack(side="top")

        self.label3 = tkinter.Label(self.bottom_frame, text="Programming Logic")
        self.label4 = tkinter.Label(self.bottom_frame, text="US History II")
        self.label5 = tkinter.Label(self.bottom_frame, text="CSCI 470")

        self.label3.pack(side="left")
        self.label4.pack(side="left")
        self.label5.pack(side="left")

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


# my_gui = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)


# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI

class MyGUI4:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.joke = tkinter.Label(self.main_window, text="HAHAHAHAHAHHAHA"
                                                         "HahAHHAHHAHHAHAH")
        self.what = tkinter.Button(self.main_window, text="What?", command=self.punchline)

        self.joke.pack()
        self.what.pack()

        tkinter.mainloop()

    def punchline(self):
        tkinter.messagebox.showinfo("Response", "Beacuse...... HAHAHAHAHHAHAH")


my_gui4 = MyGUI4()


