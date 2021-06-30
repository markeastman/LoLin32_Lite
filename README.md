# LoLin32_Lite
I wanted to explore / investigate some IoT style coding for low level sensors. After talking to a few people I purchased a Rapberry Pi 4 and was given to experiment with a LoLin32 Lite micro controller board along with a BMP280 temperature. humidy, and pressure sensor. Specific details of what I have are:
1. A Raspberyy Pi B 4GB starter kit which included a case, cables, power supply, SD card etc. But a plain Pi would work for this example.

![image](https://user-images.githubusercontent.com/1749237/123982404-ea1f5b00-d9ba-11eb-8dfb-0e5effd4d397.png)

2. A LoLin32 Lite microcontroller board - [similar to this](https://www.aliexpress.com/item/33009178296.html?spm=a2g0o.productlist.0.0.3b7e83c2eYM4Qc&aem_p4p_detail=202106300652273621360956122780025089981)
 
![image](https://user-images.githubusercontent.com/1749237/123981045-eccd8080-d9b9-11eb-8ae0-7d87e29ada70.png)

3. A Bosch BME280 temperature, humidity and pressure sensor [similar to this](https://www.amazon.co.uk/Beauneo-Compatible-Temperature-Atmospheric-Barometric/dp/B0967CWS8V/ref=sr_1_1_sspa?adgrpid=54933761882&dchild=1&gclid=EAIaIQobChMI_Kbj4MG_8QIVAWHmCh2PrgJwEAAYASAAEgLTG_D_BwE&hvadid=259027929567&hvdev=c&hvlocphy=1006948&hvnetw=g&hvqmt=b&hvrand=4946054706695607210&hvtargid=kwd-324412315802&hydadcr=5054_1827794&keywords=bmp280+sensor&qid=1625061483&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOTVEWUlNODFUUEpKJmVuY3J5cHRlZElkPUEwMzM2OTI5MlY0MTBNQlUwWEFKOSZlbmNyeXB0ZWRBZElkPUEwNDE2OTI3MUE1UDYzMEtKSUYzVCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) On the back of the chip it has a chip type of GYBMEP.

![image](https://user-images.githubusercontent.com/1749237/123980392-687afd80-d9b9-11eb-836c-e2180710dec4.png)
The specific details and data sheet for this can be [found here](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf)

Other chip sets and boards are available but I wanted to list exactly what I had and tried.
## Getting Started
As this was my first venture into the Raspberry Pi and also the microcontroller boards I searched the web and found a very good artilce titled
[Unpacking the Wemos ESP32 Lolin32 Lite, testing the firmware MicroPython with a Raspberry Pi 3](https://diyprojects.io/unpacking-wemos-esp32-lolin32-lite-testing-firmware-micropython-raspberry-pi-3/#.YNyD9i1Q1qs). Although it was for a Raspberry 3 I was gambling on it working for the Pi 4 B, which it seems to do.

The first thing to do was to connect the board to the Pi via a USB cable and then check for detection of the board via
```
dmesg | grep ttyUSB
```
however I found that I could not detect the board after trying 3 or 4 cables. I went back to the person who loaned me the board and they tried with their linux box again, they too found that it worked with some cables and not others. Once I had a working cable the Pi detected the board and could connect over ttyUSB0. I have not got to the bottom of which cabcles work and why others do not.

Within the article the first python scripts turns an led on and off but I did not have an led to try. I did find out that there is an inbuilt led on pin 22 so the very first piece of python I tried was:
```
import utime
    import machine
    pin22 = machine.Pin(22, machine.Pin.OUT)
    while True:
        pin22.value(1)
        utime.sleep_ms(500)
        pin22.value(0)
        utime.sleep_ms(500)
```
## Adding the BME280 Sensor
After many days searching the web for details on how to drive the sensor in python I came across the following useful article that pointed me to some great python code which did not need many changes. [MicroPython: Send Sensor Readings via Email (IFTTT) with ESP32 and ESP8266](https://microcontrollerslab.com/micropython-esp32-esp8266-send-sensor-readings-via-email-ifttt/)

### Pinout Diagram
The figure below shows the BME280 sensor and its pinout.
![image](https://user-images.githubusercontent.com/1749237/123993218-2905de80-d9c4-11eb-8afb-4228f1d9b0cf.png)
- VCC: connected with 3.3V
- SCL: used to generate the clock signal
- SDA: used in sending and receiving data

### Connecting the sensor to the LoLin32 Lite board
This took quite some investigations as I was not familiar with the board, nor a lot of the terminology and the fact that most articles referred to the ESP32 or ESP8266 boards.

I found a schematic for the board pinouts as:
![Lolin32_pinout03-1](https://user-images.githubusercontent.com/1749237/123993991-db3da600-d9c4-11eb-9fa6-9cf809c2d402.png)

so connecting the ground and the voltage was quite easy. The next stage was which pins to connect the SDA and SCL to. From the article it did not state the pins to use for the LoLin32 Lite SDA,SCL and so I did a further search locating this article [LOLIN32 Lite with I2C SSD1306 OLED 128×64](https://spiritdude.wordpress.com/2018/02/16/lolin32-lite-with-i2c-ssd1306-oled-128x64/) which describes how to use the I2C data transfer mechanism. According to the article the SCL should be connected to Pin 4 and SDA connected to Pin 0.

### Accessing the sensor via python
From the above article on Send Sensor Readings... there is a [link to a driver](https://raw.githubusercontent.com/robert-hh/BME280/master/bme280_int.py) which I have taken a snapshot copy of and added it to the src directory. I then copied the python file to the /pyboard folder on the microcontroller. I then main the following chnages to the main.py run file that REPL uses when a control-D is pressed. I have also added this file to the src directory.

