#!flask/bin/python
from flask import Flask
from flask import request
import json
from neopixel import *

# LED strip configuration:
LED_COUNT      = 22     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

app = Flask(__name__)
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

def setPixelColor(color):
    for i in range(0, LED_COUNT):
        strip.setPixelColor(i, color)
    strip.show()

@app.route('/test')
def index():
    return "Hello World!"

@app.route('/ambilight/color', methods=['POST'])
def set_color():
    data = request.json
    setPixelColor(Color(data['r'], data['g'], data['b']))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/ambilight/brightness', methods=['POST'])
def set_brightness():
    brightness = request.json['brightness']
    strip.setBrightness(brightness)
    strip.show()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    strip.begin()
    app.run(debug=True, host='0.0.0.0')
    setPixelColor(Color(0,0,0))
