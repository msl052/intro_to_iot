import requests

# import the RGB and Color libraries
from libraries.RGB_LED import RGB_LED
from libraries.RGB_LED.RGB_LED.Color import Color

# the address we will make the request to
# REPLACE WITH YOUR URL
settingUrl='http://intro-to-iot-lesson.herokuapp.com/api/settings'

# construct the RGB LED and Color object
red_pin = 17
green_pin = 27
blue_pin = 22
is_common_anode = True

rgb = RGB_LED.RGB_LED(red_pin,green_pin,blue_pin,is_common_anode)
color = Color()

while True:

    # make a get request to retrieve the current settings, and extract the JSON from it
    r = requests.get(settingUrl).json()
    print(r)
    lightColor = r.get(u'lightColor')
    print(str(lightColor))
    # set the color to the lightColor field of the settings object
    color.set_color_string(str(lightColor))
    
    # set the RGB's color
    print(color)
    rgb.set_color(color)