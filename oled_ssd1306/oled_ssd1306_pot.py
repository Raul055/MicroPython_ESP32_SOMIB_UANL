"""
-------------------------------------------------------------
    OLED 128x64 with SSD1306
-------------------------------------------------------------

    OLED connections:
    - VCC --> 3.3V / 5V
    - GND --> GND
    - SCL --> GPIO_25 
    - SDA --> GPIO_26 
    
    Pot Connections:
    - Extreme Pins
        -> 3.3V
        -> GND
    - Middle Pin:
        -> GPIO_33 (or any ADC pin)
    
    -- Check for other SDA/SCL for I2C communication -- 
    
"""


from machine import ADC, Pin, I2C	# Import ADC, Pin and PWM libraries, PWM for PWM in LED and ADC for POT lecture
import SSD1306		# Import SSD1306 libraty for the use of OLED
from time import sleep

adc = ADC(Pin(33))  	# Creates an ADC object
i2c = I2C(scl=Pin(25), sda=Pin(26), freq=400000)  # Use other pins for SCL and SDA
 
oled_width = 128	# State OLED width
oled_height = 64	# State OLED height
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)	# Creates OLED object

adc.atten(ADC.ATTN_11DB) 	# Attenuation (check documentation) | _11db for 3.3V input

while True:
    # ADC READ
    pot_value = adc.read() 		# Reads ADC value from POT
    print("pot value: ", pot_value) 	# Prints value in shell
    
    # OLED WRITING
    oled.fill(0)	# Fills the OLED ( 0 --> all off)
    oled.text('pot value: ' + str(pot_value), 0, 0)
    oled.show() 	# Writes in OLED (needed, if not, all previous instructions would not be done)
    sleep(0.1)	# Sleeps for 0.1 s for more stability
