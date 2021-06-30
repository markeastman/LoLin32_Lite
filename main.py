print('Running in main.py')

from machine import Pin, I2C
from BME280 import BME280

i2c = I2C(scl=Pin(4), sda=Pin(0), freq=10000)
bme280 = BME280(i2c=i2c)
bme280.values

print( "Values were printed")
