import neopixel
import board
import time
import datetime

pixels = neopixel.NeoPixel(board.D18, 12)

def clock():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    print("Hours: {0:2} Minutes: {1:2} Seconds: {2:2}".format(hour, minute, second))
    
    #Convert to 12 hour time
    if hour >= 12:
        hour -= 12
        
    #Convert values into base 12
    minute //= 5
    second //= 5
    print("Hours: {0:2} Minutes: {1:2} Seconds: {2:2}".format(hour, minute, second))
    
    #Clear LEDs
    pixels.fill((0, 0, 0))
    
    print("----Setting clock hands to LEDs----")
    #Hour:Blue Minute:Green Second:Red
    pixels[int(hour)] = (0, 0, 255)
    pixels[int(minute)] = (0, 255, 0)
    pixels[int(second)] = (255, 0, 0)

def loop():
    while(True):
        clock()
        time.sleep(1)
        
def main():
    try:
        loop() 
    except Exception:
        print("end")
        for i in range(0, 11):
            pixels[i] = (0, 0, 0)

#Start Program
main()