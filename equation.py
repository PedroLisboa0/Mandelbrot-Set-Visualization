import numpy as np
from numba import njit

@njit
def mandelbrot(original_x, original_y, max_iterations):
    x, y = original_x, original_y

    for step in range(max_iterations):
        new_x = x**2 - y**2 + original_x
        new_y = 2*x*y + original_y

        x = new_x
        y = new_y

        magnitude = np.sqrt(x**2 + y**2)

        if magnitude > 2:
            return step + 1
    return False


def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min