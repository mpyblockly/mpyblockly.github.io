<style>
.divTable{
	display: table;
	width: 100%;
  border: 0px;
}
.divTableRow {
	display: table-row;
  border: 0px;
}

.divTableCell, .divTableHead {
	border: 0px;
	display: table-cell;
	padding: 10px 50px;
  width:50%;
}

.tableHead{
	font-size: 13px;
	font-weight: 800;
	background-color: #7b8184;
	color: #fff;
}

.category{
	font-weight: 800;
}
</style>

# What is MPY Blockly?
MPY Blockly is a free visual  programming tools for Micropython on ESP32.By stacking coloured blocks on top of each other a control program can be rapidly generated. 

This simple click’n’drag programming method allows you to rapidly develop control sequences for real life microcontroller projects. This programming method is very similar to Scratch 3.

MPY Blockly also supports standard  'text' programming for those who prefer to use a text editor for programming. 

#### *MicroPython*
*<font size=2>MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.</font>*

#### *ESP32*
*<font size=2>A feature-rich MCU with integrated Wi-Fi and Bluetooth connectivity for a wide-range of applications</font>*

<img src="./assets/screenshot1.png"/>

# Why MPY Blockly?
- For beginners, use MPY Blockly to get started quickly. Even without any programming or hardware foundation. Kids and teens can also start learning programming with MPY Blockly.
- For programmers who are inexperienced in hardware, MPY Blockly can quickly drive a series of common hardware modules such as microcontrollers, various sensors, various motors, buttons, audio equipment, monochrome and color displays, RGB  strips, etc.
- Even for professionals, MPY Blockly integrates various hardware drivers (all tested in detail) and various Internet communication protocols, which can greatly reduce the development workload.

----
# Key features

<div class="divTable" style="width: 100%;" >
<div class="divTableBody">
<div class="divTableRow">
<div class="divTableCell"><img src="./assets/fi1.png" width="60"></div>
<div class="divTableCell"><img src="./assets/fi2_1.png" width="60"><img src="./assets/fi2_2.png" width="60"><img src="./assets/fi2_3.png" width="60"></div>
</div>
<div class="divTableRow">
<div class="divTableCell"><strong>Simple to use</strong></div>
<div class="divTableCell"><strong>External Components</strong></div>
</div>
<div class="divTableRow">
<div class="divTableCell">By simply dragging and dropping modules, even a beginner can quickly create works such as "Weather Station" without writing a single line of code.</div>
<div class="divTableCell">Supports many external Components, Including hundreds of  sensors, motors, audio and display devices.</div>
</div>
<div class="divTableRow">
<div class="divTableCell">&nbsp;</div>
<div class="divTableCell">&nbsp;</div>
</div>
<div class="divTableRow">
<div class="divTableCell"><img src="./assets/fi3_1.png" width="60"><img src="./assets/fi3_2.png" width="60"><img src="./assets/fi3_3.png" width="60"></div>
<div class="divTableCell"><img src="./assets/fi4_1.png" width="60"><img src="./assets/fi4_2.png" width="60"></div>
</div>
<div class="divTableRow">
<div class="divTableCell"><strong>Many protocols</strong></div>
<div class="divTableCell"><strong>Additional features</strong></div>
</div>
<div class="divTableRow">
<div class="divTableCell">Built-in support for many communication protocols such as Wifi, Bluetooth, serial port, etc. <br/>Built-in support for IoT protocols such as MQTT and Blynk<br/> Built-in support for network time synchronization, weather services and other Internet protocols.
</div>
<div class="divTableCell">Built-in code editor.<br/> Built-in serial monitor.<br/>Auto save<br/>Automatically detect serial ports
</div>
</div>
</div>
</div>



----


<!-- ## Blocks catagory

- MicroPython

| Control                                   | Text                                   | Math                                   | Variables                             | Functions                             | List                                   | Tuple                                   | Dict                                   | Set                                   | Storage                                  |
| ----------------------------------------- | -------------------------------------- | -------------------------------------- | ------------------------------------- | ------------------------------------- | -------------------------------------- | --------------------------------------- | -------------------------------------- | ------------------------------------- | ---------------------------------------- |
| <img src="./assets/icons/catControl.png"> | <img src="./assets/icons/catText.png"> | <img src="./assets/icons/catMath.png"> | <img src="./assets/icons/catVar.png"> | <img src="./assets/icons/catFun.png"> | <img src="./assets/icons/catList.png"> | <img src="./assets/icons/catTuple.png"> | <img src="./assets/icons/catDict.png"> | <img src="./assets/icons/catSet.png"> | <img src="./assets/icons/catFileDb.png"> |

- **ESP32**<br/><img src="./assets/icons/catMcu.png">System|<img src="./assets/icons/catCommunite.png">Bus|<img src="./assets/icons/catBLE.png">Bluetooth|<img src="./assets/icons/catUart.png">UART
- **External Components**<br/><img src="./assets/icons/catDispTFT.png">TFT&MONO|<img src="./assets/icons/catSegment.png">Segment LED|<img src="./assets/icon/../icons/catDispBlackWhite.png">LCD|<img src="./assets/icons/catMatrix.png">LED Matrix|<img src="./assets/icons/catNeopixel.png">Neopixel|<img src="./assets/icons/catSensor.png">Sensors|<img src="./assets/icons/catActuator.png">Actuator|<img src="./assets/icons/catMusic.png">Buzzer|<img src="./assets/icons/catAudio.png">Audio,
- **Network**<img src="./assets/icons/catNetwork.png">Network|<img src="./assets/icons/catIoT.png">IoT -->

## Features Datail

<table>
    <tr class='tableHead'>
      <td width="10%">Category</td>
      <td width="10%">Icon</td>
      <td width="80%">Description</td>
    </tr>
    <tr>
		  <td class='category'>MCU</td>
      <td><img src="./assets/icons/mcu.png" width="55px" /></td>
      <td>ESP32 Chip functions, such as Pins and GPIO, ,Touch Keys, Timer, general borad control.</td>
    </tr>
    <tr>
		  <td class='category'>Control</td>
      <td><img src="./assets/icons/control.png" width="55px" /></td>
      <td>Python If...Else, Loop and Logic.</td>
    </tr>
    <tr>
		  <td class='category'>Text</td>
      <td><img src="./assets/icons/text.png" width="55px" /></td>
      <td>Python Common string operations</td>
    </tr>
    <tr>
		  <td class='category'>Math</td>
      <td><img src="./assets/icons/math.png" width="55px" /></td>
      <td>Python Mathematical functions</td>
    </tr>
    <tr>
		  <td class='category'>Variables</td>
      <td><img src="./assets/icons/var.png" width="55px" /></td>
      <td>Python Variable</td>
    </tr>
    <tr>
		  <td class='category'>Functions</td>
      <td><img src="./assets/icons/function.png" width="55px" /></td>
      <td>Python Functions</td>
    </tr>
    <tr>
		  <td class='category'>Network</td>
      <td><img src="./assets/icons/network.png" width="55px" /></td>
      <td>ESP32 Wifi, Client, AP, Radio(ESP NOW), HTTP Client and Socket</td>
    </tr>
    <tr>
		  <td class='category'>Storage</td>
      <td><img src="./assets/icons/storage.png" width="55px" /></td>
      <td>Btree database, File operator and SD Card.</td>
    </tr>
    <tr>
		  <td class='category'>List</td>
      <td><img src="./assets/icons/list.png" width="55px" /></td>
      <td>Python Data Structre List</td>
    </tr>
    <tr>
		  <td class='category'>Tuple</td>
      <td><img src="./assets/icons/tuple.png" width="55px" /></td>
      <td>Python Data Structre Tuple</td>
    </tr>
    <tr>
		  <td class='category'>Set</td>
      <td><img src="./assets/icons/set.png" width="55px" /></td>
      <td>Python Data Structre Set</td>
    </tr>
    <tr>
		  <td class='category'>TFT&Mono</td>
      <td><img src="./assets/icons/tft.png" width="55px" /></td>
      <td>Draw functions(rect,circle,text,image...), UI functions, TFT Drivers(ST7789, ST7735, ILI9431, SSD1351, SSD1331) and Monechrome Drivers(SSD1306, SSD1106, ST7302, PCD8455).</td>
    </tr>
    <tr>
		  <td class='category'>7SegLed</td>
      <td><img src="./assets/icons/segment.png" width="55px" /></td>
      <td>TM1367 4-digit 7-segment LED display</td>
    </tr>
    <tr>
		  <td class='category'>LCD</td>
      <td><img src="./assets/icons/lcd.png" width="55px" /></td>
      <td>LCD I2C ( LCD1602/1604/2004)</td>
    </tr>
    <tr>
		  <td class='category'>LED Matrix</td>
      <td><img src="./assets/icons/matrix.png" width="55px" /></td>
      <td>MAX7219 LED Matrix</td>
    </tr>
    <tr>
		  <td class='category'>Neopixel</td>
      <td><img src="./assets/icons/neopixel.png" width="55px" /></td>
      <td>Neopixel RGB LEDs</td>
    </tr>
    <tr>
		  <td class='category'>Sensors</td>
      <td><img src="./assets/icons/sensors.png" width="55px" /></td>
      <td>Sensors include Temperature, Distance, Accelerometer, Motion Inertial, Compass, Colour, Proximity and Biometric.</td>
    </tr>
    <tr>
		  <td class='category'>Actuator</td>
      <td><img src="./assets/icons/actuator.png" width="55px" /></td>
      <td>Actuator Modules include Button, IR Remote, Rotary, Motor, Servo, Stepper, RTC, DAC, RFID and others.</td>
    </tr>
    <tr>
		  <td class='category'>Buzzer</td>
      <td><img src="./assets/icons/buzzer.png" width="55px" /></td>
      <td>Music from buzzer</td>
    </tr>
    <tr>
		  <td class='category'>Audio</td>
      <td><img src="./assets/icons/audio.png" width="55px" /></td>
      <td>Audio with I2S, Play MP3 or Wav, Record, TTS and Audio indentify.</td>
    </tr>
      <tr>
		  <td class='category'>Bus</td>
      <td><img src="./assets/icons/bus.png" width="55px" /></td>
      <td>ESP32 I2C and SPI Bus</td>
    </tr>
		  <tr>
		  <td class='category'>Bluetooth</td>
      <td><img src="./assets/icons/ble.png" width="55px" /></td>
      <td>ESP32 Bluetooth includes Perpheral, Centeral, BLE HID and BLU UART.</td>
    </tr>
		  <tr>
		  <td class='category'>UART</td>
      <td><img src="./assets/icons/uart.png" width="55px" /></td>
      <td>ESP32 UART.</td>
    </tr>
	    <tr>
		  <td class='category'>IoT</td>
      <td><img src="./assets/icons/iot.png" width="55px" /></td>
      <td>IoT functions include MQTT, Blynk and OMA Weather services.</td>
    </tr>
</table>

## Built-in supported Hardwares


<h3 id="mcu">MCU</h3>

<table>
    <tr class='tableHead'>
      <td>ESP32 devkitC 32d</td>
      <td>ESP32 devkitC 32u</td>
      <td>ESP32 devkitC Wrover</td>
      <td>ESP32 goouuuu</td>
      <td>ESP32 mini borad</td>
      <td>ESP32 nodemcu 32s</td>
		  <td>ESP32 t8 psram</td>
    </tr>
		<tr>
      <td width="14.3%"><img src="./assets/hardwares/esp32_devkitC_wroom_32d.jpg" width="150px" /></td>
      <td width="14.3%"><img src="./assets/hardwares/esp32_devkitC_wroom_32u.jpg" width="150px" /></td>
      <td width="14.3%"><img src="./assets/hardwares/esp32_devkitC_wrover.jpg" width="150px" /></td>
      <td width="14.3%"><img src="./assets/hardwares/esp32_goouuuu.jpg" width="150px" /></td>
      <td width="14.3%"><img src="./assets/hardwares/esp32_mini_borad.jpg" width="150px" /></td>
      <td width="14.3%"><img src="./assets/hardwares/esp32_nodemcu_32s.jpg" width="150px" /></td>
		  <td width="14.3%"><img src="./assets/hardwares/esp32_t8_psram.jpg" width="150px" /></td>
    </tr>
    <tr class='tableHead'>
      <td>ESP32 uno d1r32</td>
			<td>FireBeetle ESP32</td>
			<td></td>
			<td></td>
			<td></td>			
			<td></td>
			<td></td>
    </tr>
		<tr>
      <td width="14.3%"><img src="./assets/hardwares/esp32_uno_d1_r32.jpg" width="150px" /></td>
			<td width="14.3%"><img src="./assets/hardwares/FireBeetle_ESP32.jpg" width="150px" /></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
</table>

<h3 id="display---tft">Display - TFT</h3>

<table>
    <tr class='tableHead'>
      <td width="14.3%">ST7735 128x160 blue</td>
      <td width="14.3%">ST7735 128x160 red</td>
      <td width="14.3%">ST7735 128x128 red</td>
      <td width="14.3%">ST7735 80x160 blue</td>
      <td width="14.3%">ST7789 240x240</td>
      <td width="14.3%">ST7789 135x240</td>
      <td width="14.3%">SSD1351 128x128</td>
   </tr>
    <tr>
      <td><img src="./assets/hardwares/st7735_128x160_blue.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/st7735_128x160_red.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/st7735_128x128_red.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/st7735_80x160_blue.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/st7789_240x240.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/st7789_135x240.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ssd1351_128x128.jpg" width="150px" /></td>
    </tr>
</table>
<table>
    <tr class='tableHead'>
      <td width="14.3%">SSD1351 128x96</td>
      <td width="14.3%">SSD1331 96x64</td>
      <td width="14.3%">ILI9341 240x320 red</td>
      <td width="14.3%">ILI9341 240x320 blue</td>
      <td width="14.3%">                 </td>
      <td width="14.3%">                 </td>
      <td width="14.3%">                 </td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/ssd1351_128x96.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ssd1331_96x64.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ili9341_240x320.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ili9341_240x320_blue.jpg" width="150px" /></td>
      <td> </td>
      <td width="14.3%">                 </td>
      <td width="14.3%">                 </td>
    </tr>
</table>

<h3 id="display---monochrome">Display - Monochrome</h3>

<table>
    <tr class='tableHead'>
      <td width="14.3%">ssd1306 128x64</td>
      <td width="14.3%">ssd1306 128x32</td>
      <td width="14.3%">ssd1306 72x40</td>
      <td width="14.3%">ssd1106 128x64</td>
      <td width="14.3%">ssd1106 64x32</td>
      <td width="14.3%">st7302 122x250</td>
      <td width="14.3%">nokia5110 84x48</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/ssd1306_128x64.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ssd1306_128x32.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ssd1306_72x40.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ssd1106_128x64.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ssd1106_64x32.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/st7302_122x250.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/nokia5110_84x48.jpg" width="150px" /></td>
    </tr>
</table>

<h3 id="display---others">Display - Others</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">LCD 16x2</td>
      <td width="14.3%">LCD 20x4</td>
      <td width="14.3%">TM1367 segment led</td>
      <td width="14.3%">MAX7219 led matrix</td>
      <td width="14.3%">WS2812 led matrix</td>
      <td width="14.3%">WS2812 led ring</td>
      <td width="14.3%">WS2812 led strip</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/lcd1602.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/lcd2004.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/tm1367.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/mxa7219_led_matrix.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ws2812_led_matrix.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ws2812_led_ring.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ws2812_led_strip.jpg" width="150px" /></td>
    </tr>
</table>

<h3 id="sensors---temperature">Sensors - Temperature</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">DHT11 Temp Humi</td>
      <td width="14.3%">DHT22 Temp Humi</td>
      <td width="14.3%">BMP280 Temp Humi Pressure</td>
      <td width="14.3%">BMP180 Temp Humi Pressuree</td>
      <td width="14.3%">SHT3x High Accuracy Temp Humi</td>
      <td width="14.3%">DS18B20 Temp</td>
      <td width="14.3%">MLX90614  Infrared Thermometer</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/dht11.png" width="150px" /></td>
      <td><img src="./assets/hardwares/dht22.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/bmp280.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/bmp180.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/sht3x.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ds18b20.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/MLX90614.jpg" width="150px" /></td>
    </tr>
</table>

<h3 id="sensors---distanceacceleromtermotion">Sensors - Distance&amp;Acceleromter&amp;Motion</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">HC-SR04 Ultrasonic Distance</td>
      <td width="14.3%">VL53l0 ToF ranging</td>
      <td width="14.3%">VL53l1 ToF ranging</td>
      <td width="14.3%">LIS3DH 3-Axis Motion</td>
      <td width="14.3%">MPU6050 6-Axis Motion</td>
      <td width="14.3%">MPU9250  9-Axis Motion</td>
      <td width="14.3%">                 </td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/hcsr04.png" width="150px" /></td>
      <td><img src="./assets/hardwares/vl53l0.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/vl53l1.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/lis3dh.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/mpu6050.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/mpu9250.jpg" width="150px" /></td>
      <td width="14.3%">                 </td>
    </tr>
</table>

<h3 id="sensors---others">Sensors - Others</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">APDS9930 Light Proximity</td>
      <td width="14.3%">MAX30102 Oximeter Heart-Rate</td>
      <td width="14.3%">TCS3472 Color</td>
      <td width="14.3%">HMC5883l 3-Axis  Compass</td>
      <td width="14.3%">QMC5883 3-Axis Magnetic</td>
      <td width="14.3%">                 </td>
      <td width="14.3%">                 </td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/apds9930.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/max30102.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/tcs3472.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/hmc5883l.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/qmc5883.jpg" width="150px" /></td>
      <td width="14.3%">                 </td>
      <td width="14.3%">                 </td>
    </tr>
</table>


<h3 id="input---button-touch-button-joystick">Input - Button, Touch button, Joystick</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">Button</td>
      <td width="14.3%">Five buttons</td>
      <td width="14.3%">Joystick model 1</td>
      <td width="14.3%">Joystick model 2</td>
      <td width="14.3%">Touch button 1</td>
      <td width="14.3%">Touch button 4</td>
      <td width="14.3%">IR Remote</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/button_1.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/button_5.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/joystick_1.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/joystick_2.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ttp_1.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ttp_4.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ir_remote.jpg" width="150px" /></td>
    </tr>
</table>
<h3 id="motor-servo-and-stepper">Motor, Servo and Stepper</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">L298N Motor Drive Controller</td>
      <td width="14.3%">L9110S Motor Drive Controller</td>
      <td width="14.3%">L9110S-4 Motor Drive Controller</td>
      <td width="14.3%">Stepper ULN2003 Driver</td>
      <td width="14.3%">SG90 Servo 180</td>
      <td width="14.3%">SG90 Servo 360</td>
      <td width="14.3%">MG90 Servo 180/360</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/motor_l298n.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/motor_l9110s.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/motor_l9110s_4.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/stepper_uln2003.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/sg90-180.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/sg90-360.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/mg90-360.jpg" width="150px" /></td>
    </tr>
</table>
<h3 id="rtc-dac-rfid-and-relay">RTC, DAC, RFID and Relay</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">RTC DS3231</td>
      <td width="14.3%">RTC DS1307</td>
      <td width="14.3%">RTC DS1302</td>
      <td width="14.3%">DAC MCP4725</td>
      <td width="14.3%">RFID MFRC522</td>
      <td width="14.3%">Relay 1-channel</td>
      <td width="14.3%">Relay 2-channel</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/ds3231.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ds1307.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/ds1302.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/mcp4725.png" width="150px" /></td>
      <td><img src="./assets/hardwares/mfrc522.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/1-channel-5v-relay.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/2-Channel-5V-Relay.jpg" width="150px" /></td>
    </tr>
</table>

<h3 id="common-sensors">Common Sensors</h3>
<table>
    <tr class='tableHead'>
      <td width="14.3%">IR detector</td>
      <td width="14.3%">Photorezistor</td>
      <td width="14.3%">Optical barrier</td>
      <td width="14.3%">Microphone</td>
      <td width="14.3%">RCWL-0516</td>
      <td width="14.3%">PIR SB00422A-1</td>
      <td width="14.3%">PIR HC-SR505</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/IR_detector_sensor.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/photorezistor_module.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/Optical_barrier_module.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/microphone.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/Motion_detector_Microwave_Doppler_radar_RCWL-0516.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/PIR_modul_SB00422A-1.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/PIR_module_HC-SR505.jpg" width="150px" /></td>
    </tr>
</table>
<table>
    <tr class='tableHead'>
      <td width="14.3%">PIR 312</td>
      <td width="14.3%">Infrared flame</td>
      <td width="14.3%">Hall probe</td>
      <td width="14.3%">Current sensor</td>
      <td width="14.3%">TCRT5000 IRtracing</td>
      <td width="14.3%">SW-1801P shock</td>
      <td width="14.3%">Light sensor</td>
    </tr>
    <tr>
      <td><img src="./assets/hardwares/PIR_modul_PIR_module_312.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/Infrared_flame_sensor.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/Hall_probe_module.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/30A_current_sensor.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/Module_with_TCRT5000_IR_tracing_sensor.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/Module_with_SW-1801P_shock_sensor.jpg" width="150px" /></td>
      <td><img src="./assets/hardwares/Light_sensor_module.jpg" width="150px" /></td>
    </tr>
</table>
