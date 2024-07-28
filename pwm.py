"""
-------------------------------------------------------------
    PWM (Pulse Width Modulation) with LED
-------------------------------------------------------------

    Pot Connections:
    - Extreme Pins
        -> 3.3V
        -> GND
    - Middle Pin:
        -> GPIO_33 (or any ADC pin)
    
    LED Connections:
    - LED in series with resistor (220/330) to GPIO_22 (or any PWM pin) and GND
    
-------------------------------------------------------------
    
    - ADC values are 12 bits, so they take values from 0 - 4095
    - PWM values are 10 bits, so they take values from 0 - 1023
    - ADC to PWM scale is needed for correct function
    - It is divided 1023/4095, so the ADC value is multiplied (ADC*1023/4095) for scale to PWM
    
"""

from machine import ADC, Pin, PWM	# Import ADC, Pin and PWM libraries, PWM for PWM in LED and ADC for POT lecture
from time import sleep

pwm21 = PWM(Pin(21)) 	# Creates a PWM object
adc = ADC(Pin(33))  	# Creates an ADC object

adc.atten(ADC.ATTN_11DB) 	# Attenuation (check documentation) | _11db for 3.3V input

while True:
    pot_value = adc.read() 		# Reads ADC value from POT
    pwm_value = int(pot_value * (1023/4095)) 	# Scale from ADC to PWM
    print("pot value: ", pot_value, " pwm value: ", pwm_value) 	# Prints value in shell
    pwm21.duty(pwm_value)	# Duty the PWM value in PWM pin
    sleep(0.1)	# Sleeps for 0.1 s for more stability