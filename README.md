# NeopixelRing
About:

  This is a hobby project to learn about the NeoPixel Ring. 
  Currently a clock function is available but more tests and functions will be coming soon.

Hardware:

The NeoPixel is connected directly to my RaspberryPi. I soldered wires to the DC Power, Ground, and Data Input on the NeoPixel
  and connected them to the 5V Power, Ground, and GPIO Pins (4, 6, 12) 

Setup:
  1. Clone Repository
  2. Install dependencies using 'sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel'
  3. Running program using 'sudo python3 ring.py' 
