# Add your Python code here. E.g.
from microbit import *

while True:
    x = 0
    y = 0  
    for i in range(5):
        display.set_pixel(x, y, 9)
        sleep(300)
        display.set_pixel(x+1, y, 9)
        sleep(300)
        y += 1
    x = 2
    y = 4
    for i in range(5):
        display.set_pixel(x, y, 9)
        sleep(300)
        display.set_pixel(x+1, y, 9)
        sleep(300)
        y -= 1
    for i in range(5):
        display.set_pixel(4, i, 9)
        sleep(300)
    display.clear()
    sleep(300)
