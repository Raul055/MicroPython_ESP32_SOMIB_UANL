"""
-------------------------------------------------------------
    LCD 2x16 with I2C Protocol
-------------------------------------------------------------

    LCD 2x16 with I2C connections:
    - VCC --> 5V
    - GND --> GND
    - SCL --> GPIO_18 (Serial Clock)
    - SDA --> GPIO_19 (Serial Data)

"""

from machine import Pin, I2C	# Import I2C for I2C communication protocol
import esp8266_i2c_lcd as esp8266_lcd	# Import lcd libraries
from time import sleep

i2c = I2C(0)	# States I2C of canal zero (SCL-GPIO_18 / SDA-GPIO_19)
                # For more I2C config, check documentation

lcd = esp8266_lcd.I2cLcd(i2c, esp8266_lcd.DEFAULT_I2C_ADDR, 2, 16)	# Creates LCD object
                        # (I2C canal, I2C ADDR (use default), rows, columns) -- can be used for 4x20 LCD

lcd.clear()	# Cleans the LCD

counter = 0

while True:
    lcd.move_to(0,0)	# Moves to coordinate (0,0)
    lcd.putstr("2x16 LCD Demo") # Prints the string in LCD
    lcd.move_to(0,1)
    
    counter = counter + 1
    lcd.putstr(counter)
    print("Counter: %d" % (counter)) # Change from int to str is needed to print in LCD
    sleep(1)