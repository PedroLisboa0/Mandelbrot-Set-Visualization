from PIL import Image
import numpy as np
from equation import mandelbrot, map_value


width = 3840
height = 2160

white = 255
black = 0

canvas = Image.new(mode="L", size=(width, height))
pixels = canvas.load()


real_start, real_end = -2.0, 1.0

# Adjust vertical (imaginary) range based on aspect ratio
aspect_ratio = height / width
im_center = 0.0
im_range = (real_end - real_start) * aspect_ratio / 2
im_start = im_center - im_range
im_end = im_center + im_range 

for y in range(height):
    for x in range(width):
        a = map_value(x, 0, width, real_start, real_end)
        b = map_value(y, 0, height, im_start, im_end)
        explodes = mandelbrot(a, b, max_iterations=250)
        if not explodes:
            pixels[x, y] = white

canvas.save("mandelbrot_250i_correct_aspect.jpg")
