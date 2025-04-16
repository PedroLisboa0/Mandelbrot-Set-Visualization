from PIL import Image
import numpy as np
from equation import mandelbrot, map_value



width = 1000
height = 1000

white = 255
black = 0

canvas = Image.new(mode="L", size=(width, height))
pixels = canvas.load()

for y in range(height):
    for x in range(width):
        a = map_value(x, 0, width, -2, 2)
        b = map_value(y, 0, height, -2, 2)
        explodes = mandelbrot(point=(a,b), max_iterations=100)
        if not explodes:
            pixels[x+15, y] = white


   
canvas.save("mandelbrot_set.jpg")