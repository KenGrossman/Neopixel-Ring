import board
import neopixel
import time
import random

pixels = neopixel.NeoPixel(board.D18, 12)
x = 11

try:
    while(True):
#        if (x % 2 == 0):
        pixels[x] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#            time.sleep(.5)
        pixels[x] = (0, 0, 0)
        x-=1
        if(x == -1):
            x = 11
except Exception:
    print("end")
    for i in range(0, 11):
        pixels[i] = (0, 0, 0)


#def turnOffLED
