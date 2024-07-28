"""
-------------------------------------------------------------
    LCD 2x16 with OpenWeather Application
-------------------------------------------------------------

    LCD connections:
    - VCC --> 5V
    - GND --> GND
    - SCL --> GPIO_18 (Serial Clock)
    - SDA --> GPIO_19 (Serial Data)

"""

import network, usys
import urequests  as requests
import ujson as json
from machine import Pin, I2C
import esp8266_i2c_lcd as esp8266_lcd
from time import sleep

with open("/wifi_settings_openweather.json") as credentials_json:   # This pattern allows you to open and read an existing file.
    settings = json.loads(credentials_json.read())

headers = {"Content-Type": "application/json"}

url = "https://api.openweathermap.org/data/2.5/weather?id=3995465&units=metric&appid=" + settings["open_weather_key"]   # Using location ID
#url = "https://api.openweathermap.org/data/2.5/weather?q=New York,NY,US&units=metric&appid=" + settings["open_weather_key"] # Using city, state, country

def do_connect():
    wlan.active(True)                 # Activate the interface so you can use it.
    if not wlan.isconnected():        # Unless already connected, try to connect.
        print('connecting to network...')
        wlan.connect(settings["wifi_name"], settings["password"])  # Connect to the station using
                                                                   # credentials from the json file.
        if not wlan.isconnected():
            print("Can't connect to network with given credentials.")
            usys.exit(0)  # This will programmatically break the execution of this script and return to shell.
        print('network config:', wlan.ifconfig())

wlan = network.WLAN(network.STA_IF)     # This will create a station interface object.

do_connect()

if wlan.isconnected() == True:
        print("Connected")
        print("My IP address: ", wlan.ifconfig()[0])  # Prints the acquired IP address
else:
    print("Not connected")


response = requests.get(url)
weather_back = json.loads(response.content)

i2c = I2C(0) # Se usa I2C de canal cero (SCL a GPIO 18 y SDA a GPIO 19)

lcd = esp8266_lcd.I2cLcd(i2c, esp8266_lcd.DEFAULT_I2C_ADDR, 2, 16) # Constructor estandar, checar libreria esp8366_i2c_lcd si hay dudas

lcd.clear()

lcd.move_to(0,0)
lcd.putstr(weather_back["name"])
lcd.move_to(0,1)
lcd.putstr("%.2f oC" % (weather_back["main"]["temp"]))
