# main.py
from tkinter import Tk
from time import time
from config import *
from visualizer import Visualizer
from controlpanel import ControlPanel
from algorithms import *
from utils import random_list

current_milli_time = lambda: int(round(time() * 1000))

class Main(Tk):
    """The main class."""

    ALGORITHMS = {
        "Bubble": BubbleSort,
        "Bogo": BogoSort
    }

    def __init__(self):
        # Tk init
        Tk.__init__(self)
        self.title("Visualized Sorting Algorithms")
        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.resizable(False, False)

        # Sorting control variables
        self.sorting = False
        data = random_list(0, 100, 200)
        self.sort = list(self.ALGORITHMS.values())[0](data) # First algorithm

        self.sort_delay = 1000/DEFAULT_SORT_SPEED # delay, in milliseconds
        self.tick_timer = current_milli_time()

        # Visualizer init
        self.visualizer = Visualizer(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bd=0, highlightthickness=0)

        # Control panel init
        self.control_panel = ControlPanel(self)

        # Main loop
        while True:
            self.tick()

    def tick(self):
        if self.sorting:
            if current_milli_time() - self.tick_timer > self.sort_delay: # Apply sorting delay
                # Sort
                self.sort.advance_sort()
                print(self.sort.__class__.__name__, "Iteration:", self.sort.iterations)
                self.tick_timer = current_milli_time()
            
        self.visualizer.draw_data(self.sort.data, self.sort.cursor, self.sort.sorted)
        
        
        # Tk mainloop()
        self.update_idletasks()
        self.update()

    def new_algo(self, algo, min_val, max_val, size):
        data = random_list(min_val, max_val, size)
        self.sort = self.ALGORITHMS[algo](data)
        self.visualizer.algo_name = algo
        self.pause()

    def pause(self):
        self.control_panel.b_pauseplay.config(text="Play")
        self.sorting = False
    
    def play(self):
        self.control_panel.b_pauseplay.config(text="Pause")
        self.sorting = True

    def pauseplay(self):
        if self.sorting:
            self.pause()
        else:
            self.play()




if __name__ == "__main__":
    Main()