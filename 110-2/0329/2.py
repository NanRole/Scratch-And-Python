from microbit import *

while True:
  # Part 1
  for y in range(5): # 0 -> 4
    for x in range(2): # 0 1
      display.set_pixel(x, y, 9)
      sleep(300)
  # Part 2
  for y in range(4, -1, -1): # 4 -> 0
    for x in range(2, 4): # 2 3
      display.set_pixel(x, y, 9)
      sleep(300)
  # Part 3
  for y in range(5):
    display.set_pixel(4, y, 9)
    sleep(300)
  display.clear()
  sleep(300)
