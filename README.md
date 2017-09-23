# Ambilight Setup on Raspberry Pi 3
## Basic Setup
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
* now ``import neopixel`` within python scripts work


## Install Flask
* TBD install Flask

## Run Ambilight Application
* TBD

## Resources
* [WS2812 RGB LED Streifen per Raspberry Pi steuern](https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/)
* [Raspberry Pi 3 GPIO Header](https://www.element14.com/community/servlet/JiveServlet/previewBody/73950-102-11-339300/pi3_gpio.png)
* [jgarff's ws281x library](https://github.com/jgarff/rpi_ws281x)
* [WLAN config](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
* [headless mode setup](https://www.raspberrypi.org/forums/viewtopic.php?t=191252)
* [enable ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/)
* [Ubuntu 16.04 image](https://www.ubuntu.com/download/desktop/thank-you?country=CH&version=16.04.3&architecture=amd64)
* [Update Raspberry Pi](https://www.raspberrypi.org/documentation/raspbian/updating.md)
* [change passwd](https://www.raspberrypi.org/documentation/linux/usage/users.md)
