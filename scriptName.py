import requests
# import the DHT and MCP libraries
from libraries.DHT22 import DHT22
from libraries.MCP300X import MCP300X


# construct the DHT22
dht22_pin = 16
dht22 = DHT22(dht22_pin)
# construct the ldr
mcp3004 = MCP300X.MCP3004
ldr = MCP300X(mcp3004)

# the address we will make the request to
# REPLACE WITH YOUR URL
url='http://intro-to-iot-lesson.herokuapp.com/api/data'

# initialize an empty dictionary
packet = {}

# get the temperature and humidity from DHT object
humidity, temperature = dht22.get_temperature_and_humidity()

# get the brightness from the ldr object
brightness = ldr.read(ldr.CH2)

# fill the packet with data in the format expected by the web API
packet['temperature'] = round(temperature, 3)

# just a debug, comment it out when you know the script works
print(packet)

# submit the post request.
r = requests.post(url,json=packet)