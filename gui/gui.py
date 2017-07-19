"""Building gui app v 0.1"""

#pylint: disable=c0103

import tkinter as tk  # importing module tkinter which is a object itelf
from tkinter import ttk  # importing ttk from module tkinter

win = tk.Tk()  # created an instance(an object) of the class Tk named win
win.title("Python GUI")  # accessed the title mthod of the object win


# win.resizable(0, 0)  # disabling resizing

aLabel = ttk.Label(win, text="A Label")  # Creating a label
aLabel.grid(column=0, row=0)  # Managing layout


def clickMe():
    """Click Event Callback Function"""
    action.configure(text="I have been clicked")
    aLabel.configure(foreground="red")
    aLabel.configure(text="This is red now")
    # on calling this function change the button text and foreground of the label


action = ttk.Button(win, text="Click Me", command=clickMe)  # create a button
action.grid(column=1, row=0)  # button layout

win.mainloop()  # Event loop that starts the gui
