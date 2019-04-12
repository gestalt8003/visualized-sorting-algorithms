# visualizer.py
from config import *
from tkinter import *


class Visualizer(Canvas):
    """Tkinter Canvas with encapsulated fuctionality for visualization of the data."""

    def __init__(self, master, **options):
        Canvas.__init__(self, master=master, **options)
        self.master = master
        self.grid(row=0, column=0)

        self.pt_pad = 1

    def draw_data(self, data, highlight, solved=False):
        """Takes in an array of data and draws it to the screen."""
        self.delete(ALL) # Clear the drawn objects
        self.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill="black", width=0) # Blacken screen

        # DRAW

        algo_name = self.master.sort.__class__.__name__
        self.create_text(10, 10, text=algo_name, fill="white", anchor=NW)

        iteration = "Iterations: " + str(self.master.sort.iterations)
        self.create_text(10, 30, text=iteration, fill="white", anchor=NW)

        # Draw points
        pt_width = (CANVAS_WIDTH-self.pt_pad*len(data))/len(data)
        data_max = max(data)
        for i, pt in enumerate(data):
            pt_height = (pt/data_max)*(CANVAS_HEIGHT-50)
            x1 = i*(pt_width+self.pt_pad)
            y1 = CANVAS_HEIGHT
            x2 = x1+pt_width
            y2 = y1-pt_height

            color = "white"
            if i in highlight:
                color = "red"
            if solved:
                color = "green2"

            self.create_rectangle(x1, y1, x2, y2, fill=color)


