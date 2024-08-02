from machine import Pin, PWM
import network
import socket

# RGB Pin Configuration
red_pin = PWM(Pin(13)) 		# Red Pin
green_pin = PWM(Pin(23)) 	# Green Pin
blue_pin = PWM(Pin(22)) 	# Blue Pin

# Function for set RGB color
def set_color(r, g, b):
    red_pin.duty(r)
    green_pin.duty(g)
    blue_pin.duty(b)

# Connect to Wi-Fi
ssid = 'Totalplay-2.4G-2698'
password = 'KEBRjyBQQj5U4DRH'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Connection successful')
print(station.ifconfig())

# Function to handle HTTP requests
def web_page():
    html = """
    <html>
    <head>
        <title>ESP32 RGB LED Control</title>
        <style>
            body { text-align: center; font-family: "Arial"; }
            h1 { color: #0F8CFF; }
            .slider { -webkit-appearance: none; width: 100%; height: 15px; background: #d3d3d3; outline: none; }
            .value { font-size: 24px; color: #333; }
        </style>
    </head>
    <body>
        <h1>ESP32 RGB LED Control</h1>
        <p>Red: <span id="redValue" class="value">0</span></p>
        <input type="range" min="0" max="1023" value="0" class="slider" id="redRange" onchange="updateColor()">
        <p>Green: <span id="greenValue" class="value">0</span></p>
        <input type="range" min="0" max="1023" value="0" class="slider" id="greenRange" onchange="updateColor()">
        <p>Blue: <span id="blueValue" class="value">0</span></p>
        <input type="range" min="0" max="1023" value="0" class="slider" id="blueRange" onchange="updateColor()">
        <script>
            function updateColor() {
                var red = document.getElementById("redRange").value;
                var green = document.getElementById("greenRange").value;
                var blue = document.getElementById("blueRange").value;
                document.getElementById("redValue").innerText = red;
                document.getElementById("greenValue").innerText = green;
                document.getElementById("blueValue").innerText = blue;
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "/update?r=" + red + "&g=" + green + "&b=" + blue, true);
                xhr.send();
            }
        </script>
    </body>
    </html>
    """
    return html

# Setup the socket web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

print('Web server running on IP:', station.ifconfig()[0])

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    
    try:
        r = int(request.split('r=')[1].split('&')[0])
        g = int(request.split('g=')[1].split('&')[0])
        b = int(request.split('b=')[1].split(' ')[0])
        set_color(r, g, b)
    except:
        pass
    
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()