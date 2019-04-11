# visualizer.py
from config import *
from tkinter import Canvas, ALL


class Visualizer(Canvas):
    """Tkinter Canvas with encapsulated fuctionality for visualization of the data."""

    def __init__(self, master, **options):
        Canvas.__init__(self, master=master, **options)
        self.grid(row=0, column=0)

        self.sort_method = None
    

    def draw_data(self, data):
        """Takes in an array of data and draws it to the screen."""
        self.delete(ALL) # Clear the drawn objects
        self.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill="black", width=0) # Blacken screen