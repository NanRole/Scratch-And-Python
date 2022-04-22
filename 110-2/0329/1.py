# Add your Python code here. E.g.
from microbit import *

while True:
    for y in range(5):
        for x in range(5):
            if y % 2 == 0:
                display.set_pixel(x, y, 9)
            else:
                display.set_pixel(4-x, y, 9)
            sleep(300)
    display.clear()
    sleep(300)