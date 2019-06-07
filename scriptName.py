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
urlSettings='http://intro-to-iot-ece196.herokuapp.com/api/settings'
urlStats='http://intro-to-iot-ece196.herokuapp.com/api/statistics'

# initialize an empty dictionary
packet = {}

# get the temperature and humidity from DHT object
humidity, temperature = dht22.get_temperature_and_humidity()

# get the brightness from the ldr object
brightness = ldr.read(ldr.CH2)

# fill the packet with data in the format expected by the web API
packet['temperature'] = round(temperature, 3)
packet['humidity'] = round(humidity, 3)
packet['brightness'] = round(brightness, 3)
# just a debug, comment it out when you know the script works
print(packet)

# submit the post request.
r = requests.post(url,json=packet)

# get document from web api
settings = requests.get(urlSettings).json()
stats = requests.get(urlStats).json()
print(settings)
print(stats)
# make dictionary matching the format of the statistics

hotThreshold = settings.get(u'hotThreshold')
coldThreshold = settings.get(u'coldThreshold')
humidThreshold = settings.get(u'humidThreshold')
dryThreshold = settings.get(u'dryThreshold')

avgTemperature = stats.get(u'avgTemperature')
avgHumidity = stats.get(u'avgHumidity')
avgBrightness = stats.get(u'avgBrightness')
timeinHot = stats.get(u'timeinHot')
timeinCold = stats.get(u'timeinCold')
timeinDry = stats.get(u'timeinDry')
timeinHumid = stats.get(u'timeinHumid')
timeOn = stats.get(u'timeOn')
timeTotal = stats.get(u'timeTotal')

# increment the timeTotal field
timeTotal = timeTotal + 1

# increment timeIn based on threshold
if(temperature >= hotThreshold):
    timeInHot = timeInHot + 1
elif(temperature <= coldThreshold):
    timeInCold = timeInCold + 1
if(humidity <= dryThreshold):
    timeInHumid = timeInHumid + 1
elif(humidity >= dryThreshold):
    timeInDry = timeInDry + 1
    
# update the running
avgTemperature = avgTemperature + (temperature - avgTemperature)/timeTotal
avgHumidity = avgHumidity + (humidity - avgHumidity)/timeTotal
avgBrightness = avgBrightness + (brightness - avgBrightness)/timeTotal
# delete statistics
#requests.delete(urlStats)
# update new information
package = {
    'avgTemperature'    : avgTemperature,
    'avgHumidity'       : avgHumidity,
    'avgBrightness'     : avgBrightness,
    'timeinHot'         : timeinHot,
    'timeinCold'        : timeinCold,
    'timeinDry'         : timeinDry,
    'timeinHumid'       : timeinHumid,
    'timeOn'            : timeOn,
    'timeTotal'         : timeTotal
}
requests.put(urlStats,json=package)