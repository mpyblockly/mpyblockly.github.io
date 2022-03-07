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
# Features

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

|Control|Text|Math|Variables|Functions|List|Tuple|Dict|Set|Storage|
|--|--|--|--|--|--|--|--|--|--|
|<img src="./assets/icons/catControl.png">|<img src="./assets/icons/catText.png">|<img src="./assets/icons/catMath.png">|<img src="./assets/icons/catVar.png">|<img src="./assets/icons/catFun.png">|<img src="./assets/icons/catList.png">|<img src="./assets/icons/catTuple.png">|<img src="./assets/icons/catDict.png">|<img src="./assets/icons/catSet.png">|<img src="./assets/icons/catFileDb.png">|

- **ESP32**<br/><img src="./assets/icons/catMcu.png">System|<img src="./assets/icons/catCommunite.png">Bus|<img src="./assets/icons/catBLE.png">Bluetooth|<img src="./assets/icons/catUart.png">UART
- **External Components**<br/><img src="./assets/icons/catDispTFT.png">TFT&MONO|<img src="./assets/icons/catSegment.png">Segment LED|<img src="./assets/icon/../icons/catDispBlackWhite.png">LCD|<img src="./assets/icons/catMatrix.png">LED Matrix|<img src="./assets/icons/catNeopixel.png">Neopixel|<img src="./assets/icons/catSensor.png">Sensors|<img src="./assets/icons/catActuator.png">Actuator|<img src="./assets/icons/catMusic.png">Buzzer|<img src="./assets/icons/catAudio.png">Audio,
- **Network**<img src="./assets/icons/catNetwork.png">Network|<img src="./assets/icons/catIoT.png">IoT -->


## Supported Hardwares


### MCUs

|esp32 devkitC 32d|esp32 devkitC 32u|esp32 devkitC Wrover|esp32 goouuuu|esp32 mini borad|esp32 nodemcu 32s|esp32 t8 psram|esp32 uno d1r32|
|--|--|--|--|--|--|--|--|
|<img src="./assets/hardwares/esp32_devkitC_wroom_32d.jpg" width='150px'>|<img src="./assets/hardwares/esp32_devkitC_wroom_32u.jpg" width='150px'>|<img src="./assets/hardwares/esp32_devkitC_wrover.jpg" width='150px'>|<img src="./assets/hardwares/esp32_goouuuu.jpg" width='150px'>|<img src="./assets/hardwares/esp32_mini_borad.jpg" width='150px'>|<img src="./assets/hardwares/esp32_nodemcu_32s.jpg" width='150px'>|<img src="./assets/hardwares/esp32_t8_psram.jpg" width='150px'>|<img src="./assets/hardwares/esp32_uno_d1_r32.jpg" width='150px'>|

### Displays

#### TFT

|st7735 128x160 blue|st7735 128x160 red|st7735 128x128 red|st7735 80x160 blue|st7789 240x240|st7789 135x240|ili9341 240x320 red|ili9341 240x320 blue|
|--|--|--|--|--|--|--|--|
|<img src="./assets/hardwares/st7735_128x160_blue.jpg" width='150px'>|<img src="./assets/hardwares/st7735_128x160_red.jpg" width='150px'>|<img src="./assets/hardwares/st7735_128x128_red.jpg" width='150px'>|<img src="./assets/hardwares/st7735_80x160_blue.jpg" width='150px'>|<img src="./assets/hardwares/st7789_240x240.jpg" width='150px'>|<img src="./assets/hardwares/st7789_135x240.jpg" width='150px'>|<img src="./assets/hardwares/ili9341_240x320.jpg" width='150px'>|<img src="./assets/hardwares/ili9341_240x320_blue.jpg" width='150px'>|