"""
-------------------------------------------------------------
    OLED 128x64 with SSD1306
-------------------------------------------------------------

    OLED connections:
    - VCC --> 3.3V / 5V
    - GND --> GND
    - SCL --> GPIO_25 
    - SDA --> GPIO_26 
    
    -- Check for other SDA/SCL for I2C communication -- 
    
"""


from machine import Pin, SoftI2C 	# Use SoftI2C library for the use of other I2C pin communication 
import SSD1306		# Import SSD1306 libraty for the use of OLED
from time import sleep
 
i2c = SoftI2C(scl=Pin(25), sda=Pin(26), freq=400000)  # Use other pins for SCL and SDA
 
oled_width = 128	# State OLED width
oled_height = 64	# State OLED height
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)	# Creates OLED object
 
while True:
    oled.fill(0)	# Fills the OLED ( 0 --> all off)
    oled.text('Welcome', 0, 0)	# Put str in (0,0) coordinate 
    oled.text('OLED Display', 0, 10)
    oled.text('line 3', 0, 20)
    oled.text('line 4', 0, 30)        
    oled.show() 	# Writes in OLED (needed, if not, all previous instructions would not be done)
    sleep(3)
    oled.fill(1)		# Fills the OLED ( 1 --> all on)
    oled.show()
    sleep(3)
    oled.fill(0)
    oled.show()
    sleep(3)
    oled.line(0,0,110,50,1) 	# Draws line (check documentation)
    oled.show()
    sleep(3)
