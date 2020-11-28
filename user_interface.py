""" This module opens a popup box to get the 
    input value of alarm time from the user    
"""
from tkinter import *
import tkinter as tk

from main_function import *

def show_entry_fields():
    """ This function gets the inout value from the UI button
        Provides the input value to my_main_function and calls it    
    """

    set_alarm_timer = e1.get()
    my_main_function(set_alarm_timer)


master = tk.Tk()
master.title("Reminder Clock")

tk.Label(master, 
         text="Time").grid(row=0)

e1 = tk.Entry(master)
e1.grid(row=0, column=1)


tk.Button(master, 
          text='Set', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()