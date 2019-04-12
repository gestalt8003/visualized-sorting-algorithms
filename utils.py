# utils.py
from random import randint



def random_list(min_val, max_val, size):
    """Generates a random list of integers from min_val to max_val (inclusive) of size size."""
    data = []
    for i in range(size):
        data.append(randint(min_val, max_val))
    return data