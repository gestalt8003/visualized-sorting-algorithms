# controlpanel.py
from config import *
from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import Combobox

class ControlPanel(Frame):
    """Allows the user to control elements of the sorting algorithm."""

    def __init__(self, master, **options):
        Frame.__init__(self, master=master, **options)
        self.master = master
        self.grid(row=1, column=0)
        self.config(padx=5, pady=5)

        Label(self, text="Algorithm:").pack(side=LEFT)
        self.combo_algo = Combobox(self, values=list(master.ALGORITHMS.keys()))
        self.combo_algo.current(0)
        self.combo_algo.bind("<<ComboboxSelected>>", self.restart)
        self.combo_algo.pack(side=LEFT, padx=(2, 5))

        self.b_restart = Button(self, text="Restart (new data)", command=self.restart)
        self.b_restart.pack(side=LEFT, padx=(5, 0))

        self.b_pauseplay = Button(self, text="Play", command=master.pauseplay)
        self.b_pauseplay.pack(side=LEFT, padx=(0, 5))

        self.scl_speed = Scale(self, from_=1, to=100, 
                            orient=HORIZONTAL, sliderlength=10, showvalue=0,
                            length=125,
                            label="Speed: 30 iters/s", command=self.change_speed)
        self.scl_speed.set(30)
        self.scl_speed.pack(side=LEFT, padx=5)

    def query_params(self):
        min_val = simpledialog.askinteger("Input", "Minimum value:",
                                        parent=self.master,
                                        initialvalue=0)
        if min_val is None:
            return None
        max_val = simpledialog.askinteger("Input", "Maximum value:",
                                        parent=self.master,
                                        minvalue=min_val,
                                        initialvalue=min_val+100)
        size = simpledialog.askinteger("Input", "Size of data:",
                                        parent=self.master,
                                        minvalue=2,
                                        initialvalue=100)
        if max_val is None or size is None:
            return None
        return min_val, max_val, size

    def restart(self, e=None):
        min_val, max_val, size = self.query_params()
        self.master.new_algo(self.combo_algo.get(), min_val, max_val, size)

    def change_speed(self, e=None):
        speed = self.scl_speed.get()
        self.master.sort_delay = 1000/speed
        self.scl_speed.config(label="Speed: {} iters/s".format(speed))
        print("Sort speed:", self.scl_speed.get())