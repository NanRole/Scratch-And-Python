from microbit import *

sleep_time = 1000

while True:
  for i in range(4, -1, -1):
    # |
    for j in range(5-i):
      display.set_pixel(i, j, 9)
    # ——
    for j in range(i, 5):
      display.set_pixel(j, 4-i, 9)
    sleep(sleep_time)
  for i in range(0, 5):
    for j in range(5-i):
      display.set_pixel(i, j, 0)
    for j in range(i, 5):
      display.set_pixel(j, 4-i, 0)
    sleep(sleep_time)
  display.clear()
  sleep(sleep_time)
