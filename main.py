# main.py
from tkinter import Tk
import time
from config import *
from visualizer import Visualizer
from controlpanel import ControlPanel

current_milli_time = lambda: int(round(time.time() * 1000))

class Main(Tk):
    """The main class."""

    def __init__(self):
        # Tk init
        Tk.__init__(self)
        self.title("Visualized Sorting Algorithms")
        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.resizable(False, False)

        # Sorting control variables
        self.sorting = False

        self.sort_delay = 1000/DEFAULT_SORT_SPEED # delay, in milliseconds
        self.tick_timer = current_milli_time()

        # Visualizer init
        self.visualizer = Visualizer(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bd=0, highlightthickness=0)
        self.visualizer.draw_data(0)

        # Control panel init
        self.control_panel = ControlPanel(self)

        # Main loop
        while True:
            self.tick()

    def tick(self):
        if self.sorting:
            if current_milli_time() - self.tick_timer > self.sort_delay: # Apply sorting delay
                # Sort
                print("sort loop")
                self.tick_timer = current_milli_time()

        # Tk mainloop()
        self.update_idletasks()
        self.update()







if __name__ == "__main__":
    Main()