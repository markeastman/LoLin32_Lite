# LoLin32_Lite
I wanted to explore / investigate some IoT style coding for low level sensors. After talking to a few people I purchased a Rapberry Pi 4 and was given to experiment with a LoLin32 Lite micro controller board along with a BMP280 temperature. humidy, and pressure sensor. Specific details of what I have are:
1. A Raspberyy Pi B 4GB starter kit which included a case, cables, power supply, SD card etc. But a plain Pi would work for this example.

![image](https://user-images.githubusercontent.com/1749237/123982404-ea1f5b00-d9ba-11eb-8dfb-0e5effd4d397.png)

2. A LoLin32 Lite microcontroller board - [similar to this](https://www.aliexpress.com/item/33009178296.html?spm=a2g0o.productlist.0.0.3b7e83c2eYM4Qc&aem_p4p_detail=202106300652273621360956122780025089981)
 
![image](https://user-images.githubusercontent.com/1749237/123981045-eccd8080-d9b9-11eb-8ae0-7d87e29ada70.png)

3. A Bosch BME280 temperature, humidity and pressure sensor [similar to this](https://www.amazon.co.uk/Beauneo-Compatible-Temperature-Atmospheric-Barometric/dp/B0967CWS8V/ref=sr_1_1_sspa?adgrpid=54933761882&dchild=1&gclid=EAIaIQobChMI_Kbj4MG_8QIVAWHmCh2PrgJwEAAYASAAEgLTG_D_BwE&hvadid=259027929567&hvdev=c&hvlocphy=1006948&hvnetw=g&hvqmt=b&hvrand=4946054706695607210&hvtargid=kwd-324412315802&hydadcr=5054_1827794&keywords=bmp280+sensor&qid=1625061483&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOTVEWUlNODFUUEpKJmVuY3J5cHRlZElkPUEwMzM2OTI5MlY0MTBNQlUwWEFKOSZlbmNyeXB0ZWRBZElkPUEwNDE2OTI3MUE1UDYzMEtKSUYzVCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) On the back of the chip it has a chip type of GYBMEP.

![image](https://user-images.githubusercontent.com/1749237/123980392-687afd80-d9b9-11eb-836c-e2180710dec4.png)


Other chip sets and boards are available but I wanted to list exactly what I had and tried.
## Getting Started
As this was my first venture into the Raspberry Pi and also the microcontroller boards I searched the web and found a very good artilce titled
[Unpacking the Wemos ESP32 Lolin32 Lite, testing the firmware MicroPython with a Raspberry Pi 3](https://diyprojects.io/unpacking-wemos-esp32-lolin32-lite-testing-firmware-micropython-raspberry-pi-3/#.YNyD9i1Q1qs). Although it was for a Raspberry 3 I was gambling on it working for the Pi 4 B, which it seems to do.

I did not have an led to try the first code to drive the board but I did find out that there is an inbuilt led on pin 22 so the very first piece of python I tried was
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


