from microbit import *

while True:
  for i in range(5):
    for j in range(i+1):
      display.set_pixel(i-j, j, 9)
      sleep(300)
  for i in range(4):
    for j in range(4, i, -1):
      display.set_pixel(j, 5+i-j, 9)
      sleep(300)
  display.clear()
  sleep(300)