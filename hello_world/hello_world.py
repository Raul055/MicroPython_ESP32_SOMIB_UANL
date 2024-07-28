"""
-------------------------------------------------------------
    Hello World
-------------------------------------------------------------

    - Connect LED with resistor (220/330) in series to GPIO and GND

"""

from machine import Pin 	# Import 'machine' library for Pin use
from time import sleep 		# Import 'time' for sleep function

led = Pin(29, Pin.OUT)		# Declares led object for its use --> (GPIO_PIN, Pin.OUT/Pin.In)

while True:		# While infinite loop (as a 'void loop()' function from arduino)
    led.on()	# States the led object to 1 (or high)
    sleep(1)	# Sleeps for 1 second (delay)
    led.off()	# States the led object to 0 (or low)
    sleep(1)
    
