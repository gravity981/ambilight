# AmbiLight with Raspberry Pi 3, WS2812 LEDs and Python
AmbiLight consists of a Server and a Client application.
At the moment it is possible to set static colors with a Client Python application
Ideas to implement in the future
* find a performant way to grab "average" screen color and update light in realtime
* system tray app for windows
* bind music to some kind of color effect
* implement some effects (server based) select with client app
* investigate performance gain of UDP data transmission instead of http requests

## Basic Setup Rasperry Pi
* flash [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) to Raspberry Pi's SD card, on windows use [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/)
  * used version: 2017-09-07-raspbian-stretch-lite
* Connect SD card to computer and open boot partition (works also on windows)
* create empty file called ``ssh`` on boot partition. on next reboot ssh will be enabled
* for WLAN connection create another file called ``wpa_supplicant.conf`` with the following content:

```
country=CH
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="your_real_wifi_ssid"
    scan_ssid=1
    psk="your_real_password"
    key_mgmt=WPA-PSK
}
```
* plugin SD card to Raspberry Pi and power up
* connect via ssh
  * default hostname is ``raspberrypi``
  * default user is ``pi``
  * default password is ``raspberry``
* ``sudo apt-get update``
* ``sudo apt-get dist-upgrade``
* ``sudo nano /etc/hostname`` and change hostname to ``amlipi``
* ``sudo passwd pi`` to change pi's password

## Install Driver for WS2812B LEDs
* ``sudo apt-get install git``
* make sure you're in home directory, then ``git clone https://github.com/jgarff/rpi_ws281x``
* ``nano rpi_ws281x/main.c``, depending on the number and configuration of your WS2812 LEDs change ``WIDTH`` and ``HEIGHT``
* ``sudo apt-get install scons``
* ``cd rpi_ws281x``
* ``scons`` to build library
* make sure LEDs are connected correctly (default DIN is GPIO 18)
* ``sudo ./test -c`` to check if LEDs work
* now build python wrapper
  * ``sudo apt-get install python-dev swig``
  * ``cd ~/rpi_ws281x/python/``
  * ``python ./setup.py build``
* ``nano ~/.bashrc`` in pi home directory
* add ``export PYTHONPATH="${PYTHONPATH}:/home/pi/rpi_ws281x/python/build/lib.linux-armv7l-2.7"`` at the end
* ``source ~/.bashrc``
* driver needs access to /dev/mem, thats why scripts with LEDs must be called with sudo
  * ``sudo nano /etc/sudoers``
  * add ``Defaults env_keep += "PYTHONPATH"`` in the end
* now ``import neopixel`` within python scripts should work


## Install Flask Python Web Framework
* ``sudo apt-get install python-pip``
* ``sudo pip install flask``


## Run Ambilight Server Application
* Manual Launch
  * copy ``AmbiLightServer.py`` to ``/home/pi/`` on your Raspberry Pi (on Windows
    with e.g. [WinSCP](https://winscp.net/eng/docs/lang:de))
  * ``sudo python AmbiLightServer.py`` to launch application
  * The server listens on **Port 5000** per default

# REST API

## /ambilight/color
This resource can be used to set the color of all LEDs simultaneously
* method: POST
* contentType: application/json
* data format:
```
{
    "r": <0-255>,
    "g": <0-255>,
    "b": <0-255>
}
```

## /ambilight/brightness
This resource can be used to set the brightness of all LEDs simultaneously
* method: POST
* contentType: application/json
* data format:
```
{
    "brightness": <0-255>
}
```

# Run the Python AmbiLightClient
* on your client computer python ``requests`` library must be installed
* ``pip install requests``
* ``python AmbiLightClient.py`` to run

# Moar
* [WS2812 RGB LED Streifen per Raspberry Pi steuern](https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/)
* [Raspberry Pi 3 GPIO Header](https://www.element14.com/community/servlet/JiveServlet/previewBody/73950-102-11-339300/pi3_gpio.png)
* [jgarff's ws281x library](https://github.com/jgarff/rpi_ws281x)
* [WLAN config](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
* [headless mode setup](https://www.raspberrypi.org/forums/viewtopic.php?t=191252)
* [enable ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/)
* [Ubuntu 16.04 image](https://www.ubuntu.com/download/desktop/thank-you?country=CH&version=16.04.3&architecture=amd64)
* [Update Raspberry Pi](https://www.raspberrypi.org/documentation/raspbian/updating.md)
* [change passwd](https://www.raspberrypi.org/documentation/linux/usage/users.md)
* [Designing RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [ScreenBloom](http://www.screenbloom.com/)
* [Autonomous Light Controller](http://klautesblog.blogspot.ch/2013/03/autonomous-light-controller.html)
