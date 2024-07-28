"""
-------------------------------------------------------------
    DHT22
-------------------------------------------------------------

    DHT22 Connections:
    - VCC --> 3.3V
    - GND --> GND
    - DATA --> GPIO_25
    - NC --> NO CONNECT

"""

from machine import Pin, Timer # Import libraries for Pin and Timer (use of timers)
import dht	# Import DHT library (can use DHT11 module)

dht22 = dht.DHT22(Pin(25))	# Creates DHT22 object in GPIO25

def take_measurment_isr(event):		# Creates 'take_measurement_isr' for timer use
    dht22.measure()		# Collect the data from DATA pin
    tempC = dht22.temperature() 	# Stores the temperature in tempC variable (temperature in °C)
    tempF = ((9/5)*tempC) + 32		# Celcius to Farenheit conversion
    print("Temperature: ", tempC, "°C", " Temperature: ", tempF, "°F"," Humidity: ", dht22.humidity(), "%") # Prints both temperatures

dht_timer = Timer(1)	# Creates timer
dht_timer.init(period=500, mode=Timer.PERIODIC, callback=take_measurment_isr)	# Timer init

"""
    ------------------------
    Timer.init conditions:
    ------------------------
    --> period = time in ms
    --> mode = Timer.ONE_SHOT (do the timer one time) / Timer.Periodic (do the timer several times as a while True loop)
    --> callback = callback function
"""
