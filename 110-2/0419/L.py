from microbit import *

while True:
  for i in range(4, -1, -1):
    for j in range(5-i):
      display.set_pixel(i, j, 9)
    for j in range(i+1, 5):
      display.set_pixel(j, 4-i, 9)
    sleep(300)
  for i in range(0, 5):
    for j in range(5-i):
      display.set_pixel(i, j, 0)
    for j in range(i+1, 5):
      display.set_pixel(j, 4-i, 0)
    sleep(300)
  display.clear()
  sleep(300)