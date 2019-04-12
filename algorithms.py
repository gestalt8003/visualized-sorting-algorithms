# algorithms.py
from random import *

class Sort:

    def __init__(self, data):
        self.data = data
        self.iterations = 0
        self.sorted = False
        self.cursor = [] # For visualization, highlights elements of array

        self.n = len(data)

    def advance_sort(self):
        self.iterations += 1


class BubbleSort(Sort):
    
    def __init__(self, data):
        Sort.__init__(self, data)
        print(__class__.__name__)
        self.i = 0

    def advance_sort(self):
        if not self.sorted:
            Sort.advance_sort(self)

            self.cursor.clear()

            if self.i < self.n:
                for j in range(0, self.n-self.i-1):
                    if self.data[j] > self.data[j+1]:
                        self.cursor.extend([j, j+1])
                        self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
            
                self.i += 1
            else:
                self.sorted = True
        

class BogoSort(Sort):
    
    def __init__(self, data):
        Sort.__init__(self, data)
        print(__class__.__name__)

    def advance_sort(self):
        if not self.sorted:
            Sort.advance_sort(self)

            self.cursor.clear()
            self.cursor.extend(range(0, self.n))

            shuffle(self.data)

            self.sorted = True
            for j in range(0, self.n-1):
                if self.data[j] < self.data[j+1]:
                    self.sorted = False