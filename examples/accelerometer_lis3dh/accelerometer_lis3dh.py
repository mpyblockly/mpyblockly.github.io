from machine import SoftI2C, PWM, Pin, ADC,I2C

i2c = I2C(0,scl=Pin(22), sda=Pin(23), freq=100000)

from  lis3dh import *
_lis3dh = lis3dh(i2c)
while True:
  print(''.join([str(x) for x in [0, ',', _lis3dh.getXDegree(), ',', _lis3dh.getYDegree()]]))