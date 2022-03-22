from machine import I2C,SoftI2C, PWM, Pin, ADC

from machine import SPI

from dr.st7735.st7735_16bit import ST7735
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13))
_st7735  = ST7735(spi,0,15,None,128,160,rotate=2)
_st7735.initb2()
_st7735.setrgb(True)

from gui.colors import colors
_color = colors(_st7735)

from dr.display import display
_dis = display(_st7735,'ST7735_FB',_color.WHITE,_color.BLACK)
_dis.fill(_color.BLACK)
_dis.dev.show()

from mpyb_wifi import *

import network

my_wifi = wifi()

import ntptime

from weather import owm_get_weather

import time

import datetimeformat

from pngdecode import png_decode

import framebuf

import fonts.spleen16 as spleen16

import fonts.digiface30 as digiface30

import fonts.spleen24 as spleen24

from fonts.icons import draw_icon

import fonts.system8 as system8

import machine

myUI = UI(oled)
try:
  my_wifi.connectWiFi('mpyblockly', 'mpyblockly')
  ntptime.settime(0, "time.windows.com")
  weatherinfo= owm_get_weather(51.48,(-0.11),'d2f2bb0c1e94e5aef3c9f4f60d51f162',"metric")
  while True:
    if (time.localtime()[4]) % 10 == 0:
      weatherinfo= owm_get_weather(51.48,(-0.11),'d2f2bb0c1e94e5aef3c9f4f60d51f162',"metric")
    _dis.fill()
    (_png_buf,_png_w,_png_h) = png_decode((''.join([str(x) for x in ['/resources/images/weathericons/60/black/', weatherinfo["current"]["weather"][0]["icon"], '.png']])))
    _png_fbc = framebuf.FrameBuffer(_png_buf, _png_w,_png_h, framebuf.RGB565)
    _dis.dev.blit(_png_fbc,2,2)
    _dis.draw_text(spleen16,'London',66,8,1,_dis.fgcolor,_dis.bgcolor,0,False,0,0)
    _dis.draw_text(spleen16,(weatherinfo["current"]["weather"][0]["main"]),66,32,1,_dis.fgcolor,_dis.bgcolor,0,True,0,0)
    _dis.draw_text(digiface30,(''.join([str(x2) for x2 in [datetimeformat.get_datetime_left_aligns_zero()[3], ':', datetimeformat.get_datetime_left_aligns_zero()[4]]])),6,66,1,_dis.fgcolor,_dis.bgcolor,0,True,0,0)
    _dis.set_fgcolor(_dis.dev.TFTColor(255,204,102))
    _dis.draw_text(spleen24,(datetimeformat.get_datetime_left_aligns_zero()[5]),93,76,1,_dis.fgcolor,_dis.bgcolor,0,True,0,0)
    _dis.set_fgcolor(_dis.dev.TFTColor(255,255,255))
    _dis.draw_text(spleen24,(''.join([str(x3) for x3 in [datetimeformat.get_datetime_left_aligns_zero()[2], '/', datetimeformat.get_datetime_left_aligns_zero()[1], ' ', datetimeformat.get_weekday_name((time.localtime()[6]))[1]]])),6,104,1,_dis.fgcolor,_dis.bgcolor,0,True,0,0)
    _dis.set_fgcolor(_dis.dev.TFTColor(255,102,0))
    draw_icon(28,_dis,2,132,1,_dis.fgcolor,_dis.bgcolor,1);
    myUI.ProgressBar(14, 132, 68, 8, (1 * (weatherinfo["current"]["temp"])))
    _dis.set_fgcolor(_dis.dev.TFTColor(255,255,255))
    _dis.draw_text(system8,(str(weatherinfo["current"]["temp"]) + 'C'),84,132,1,_dis.fgcolor,_dis.bgcolor,0,True,0,0)
    _dis.set_fgcolor(_dis.dev.TFTColor(51,204,255))
    draw_icon(27,_dis,2,147,1,_dis.fgcolor,_dis.bgcolor,1);
    myUI.ProgressBar(14, 147, 68, 8, (weatherinfo["current"]["humidity"]))
    _dis.set_fgcolor(_dis.dev.TFTColor(255,255,255))
    _dis.draw_text(system8,(str(weatherinfo["current"]["humidity"]) + '%'),84,147,1,_dis.fgcolor,_dis.bgcolor,0,True,0,0)
    _dis.dev.show()
    time.sleep(1)


except Exception as ex:
  machine.reset()