# controlpanel.py
from config import *
from tkinter import Frame, Button, Label

class ControlPanel(Frame):
    """Allows the user to control elements of the sorting algorithm."""

    def __init__(self, master, **options):
        Frame.__init__(self, master=master, **options)
        self.grid(row=1, column=0)
        self.config(padx=5, pady=5)

        l = Label(master=self, text="Test")
        l.pack(padx=5, pady=5, anchor='w')