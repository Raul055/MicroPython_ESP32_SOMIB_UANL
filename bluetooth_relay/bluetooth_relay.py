"""
-------------------------------------------------------------
    Relay Control with Bluetooth
-------------------------------------------------------------

    Control Connection - 2n3904 Transistor Connections:
    - 1k resistor between any GPIO pin to base
    - 1k resistor between VCC (5V) and collector
    - Emmiter to GND
    
    Relay Connections:
    - Coil 1 to collector
    - Coil 2 to VCC (5V)
    --> No importance between coils (coil 1 can be coil 2 and viceversa)
    
    Power Connections:
    - Common pin from relay to base bulb
    - Live/Neutral wire to base bulb (just one)
    - NC pin to base bulb
    
"""

from machine import Pin 	# Import for GPIO use
import bluetooth 	# Import for bluetooth communication
from BLE import BLEUART		# Import for uart bluetooth communication

# Pins declaration
relay = Pin(25, Pin.OUT) 	# Relay Pin
on_pin = Pin(23, Pin.OUT) 	# On Pin
off_pin = Pin(12, Pin.OUT) 	# Off Pin

# Init Bluetooth
name = "ESP32 Raul" 	# Bluetooth Name Board
ble = bluetooth.BLE() 	# Bluetooth Instance
uart = BLEUART(ble, name) 	# Bluetooth Object

# Bluetooth RX Event
def on_rx():	# Function for TX<->RX communication
    rx_buffer = uart.read().decode().strip()
    
    """
    .read() = reads the uart serial port
    .decode() = decodes the sent string (needed for serial bluetooth communication)
    .strip() = removes spaces at the beginning and end of the string
    """
    # UART writing
    uart.write('Your message was: ' + str(rx_buffer) + '\n') 	# Writes the given message
    
    action = rx_buffer.lower()
    
    if action == "on":
        relay.on()
        on_pin.on()
        off_pin.off()
        uart.write('The light bulb is on')
    elif action == "off":
        relay.off()
        on_pin.off()
        off_pin.on()
        uart.write('The light bulb is off')

# Registers Bluetooth Event
uart.irq(handler=on_rx) 
