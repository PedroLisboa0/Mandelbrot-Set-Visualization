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
        a = map_value(x, 0, width, -2, 1)
        b = map_value(y, 0, height, -1.5, 1.5)
        explodes = mandelbrot(a, b, max_iterations=10)
        if not explodes:
            pixels[x+25, y] = white


   
canvas.save("mandelbrot_10i.jpg")