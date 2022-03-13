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

| Control                                   | Text                                   | Math                                   | Variables                             | Functions                             | List                                   | Tuple                                   | Dict                                   | Set                                   | Storage                                  |
| ----------------------------------------- | -------------------------------------- | -------------------------------------- | ------------------------------------- | ------------------------------------- | -------------------------------------- | --------------------------------------- | -------------------------------------- | ------------------------------------- | ---------------------------------------- |
| <img src="./assets/icons/catControl.png"> | <img src="./assets/icons/catText.png"> | <img src="./assets/icons/catMath.png"> | <img src="./assets/icons/catVar.png"> | <img src="./assets/icons/catFun.png"> | <img src="./assets/icons/catList.png"> | <img src="./assets/icons/catTuple.png"> | <img src="./assets/icons/catDict.png"> | <img src="./assets/icons/catSet.png"> | <img src="./assets/icons/catFileDb.png"> |

- **ESP32**<br/><img src="./assets/icons/catMcu.png">System|<img src="./assets/icons/catCommunite.png">Bus|<img src="./assets/icons/catBLE.png">Bluetooth|<img src="./assets/icons/catUart.png">UART
- **External Components**<br/><img src="./assets/icons/catDispTFT.png">TFT&MONO|<img src="./assets/icons/catSegment.png">Segment LED|<img src="./assets/icon/../icons/catDispBlackWhite.png">LCD|<img src="./assets/icons/catMatrix.png">LED Matrix|<img src="./assets/icons/catNeopixel.png">Neopixel|<img src="./assets/icons/catSensor.png">Sensors|<img src="./assets/icons/catActuator.png">Actuator|<img src="./assets/icons/catMusic.png">Buzzer|<img src="./assets/icons/catAudio.png">Audio,
- **Network**<img src="./assets/icons/catNetwork.png">Network|<img src="./assets/icons/catIoT.png">IoT -->


## Built-in supported Hardwares


### MCU

<table>
    <tr>
      <td>esp32 devkitC 32d</td>
      <td>esp32 devkitC 32u</td>
      <td>esp32 devkitC Wrover</td>
      <td>esp32 goouuuu</td>
      <td>esp32 mini borad</td>
      <td>esp32 nodemcu 32s</td>
    </tr>
		<tr>
      <td width='12.5%'><img src="./assets/hardwares/esp32_devkitC_wroom_32d.jpg" width="150px" /></td>
      <td width='12.5%'><img src="./assets/hardwares/esp32_devkitC_wroom_32u.jpg" width="150px" /></td>
      <td width='12.5%'><img src="./assets/hardwares/esp32_devkitC_wrover.jpg" width="150px" /></td>
      <td width='12.5%'><img src="./assets/hardwares/esp32_goouuuu.jpg" width="150px" /></td>
      <td width='12.5%'><img src="./assets/hardwares/esp32_mini_borad.jpg" width="150px" /></td>
      <td width='12.5%'><img src="./assets/hardwares/esp32_nodemcu_32s.jpg" width="150px" /></td>
    </tr>
		<tr>
		  <td>esp32 t8 psram</td>
      <td>esp32 uno d1r32</td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>			
    </tr>
		<tr>
		  <td width='12.5%'><img src="./assets/hardwares/esp32_t8_psram.jpg" width="150px" /></td>
      <td width='12.5%'><img src="./assets/hardwares/esp32_uno_d1_r32.jpg" width="150px" /></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
</table>

| esp32 devkitC 32d                                                        | esp32 devkitC 32u                                                        | esp32 devkitC Wrover                                                  | esp32 goouuuu                                                  | esp32 mini borad                                                  | esp32 nodemcu 32s                                                  | esp32 t8 psram                                                  | esp32 uno d1r32                                                   |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | --------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------- |
| <img src="./assets/hardwares/esp32_devkitC_wroom_32d.jpg" width='150px'> | <img src="./assets/hardwares/esp32_devkitC_wroom_32u.jpg" width='150px'> | <img src="./assets/hardwares/esp32_devkitC_wrover.jpg" width='150px'> | <img src="./assets/hardwares/esp32_goouuuu.jpg" width='150px'> | <img src="./assets/hardwares/esp32_mini_borad.jpg" width='150px'> | <img src="./assets/hardwares/esp32_nodemcu_32s.jpg" width='150px'> | <img src="./assets/hardwares/esp32_t8_psram.jpg" width='150px'> | <img src="./assets/hardwares/esp32_uno_d1_r32.jpg" width='150px'> |

### Display - TFT

| st7735 128x160 blue                                                  | st7735 128x160 red                                                  | st7735 128x128 red                                                  | st7735 80x160 blue                                                  | st7789 240x240                                                  | st7789 135x240                                                  |
| -------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| <img src="./assets/hardwares/st7735_128x160_blue.jpg" width='150px'> | <img src="./assets/hardwares/st7735_128x160_red.jpg" width='150px'> | <img src="./assets/hardwares/st7735_128x128_red.jpg" width='150px'> | <img src="./assets/hardwares/st7735_80x160_blue.jpg" width='150px'> | <img src="./assets/hardwares/st7789_240x240.jpg" width='150px'> | <img src="./assets/hardwares/st7789_135x240.jpg" width='150px'> |

| ssd1351 128x128                                                  | ssd1351 128x96                                                  | ssd1331 96x64                                                  | ili9341 240x320 red                                              | ili9341 240x320 blue                                                  | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| ---------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| <img src="./assets/hardwares/ssd1351_128x128.jpg" width='150px'> | <img src="./assets/hardwares/ssd1351_128x96.jpg" width='150px'> | <img src="./assets/hardwares/ssd1331_96x64.jpg" width='150px'> | <img src="./assets/hardwares/ili9341_240x320.jpg" width='150px'> | <img src="./assets/hardwares/ili9341_240x320_blue.jpg" width='150px'> |

### Display - Monochrome

| ssd1306 128x64                                                  | ssd1306 128x32                                                  | ssd1306 72x40                                                  | ssd1106 128x64                                                  | ssd1106 64x32                                                  | st7302 122x250                                                  | nokia5110 84x48                                                  |
| --------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------- |
| <img src="./assets/hardwares/ssd1306_128x64.jpg" width='150px'> | <img src="./assets/hardwares/ssd1306_128x32.jpg" width='150px'> | <img src="./assets/hardwares/ssd1306_72x40.jpg" width='150px'> | <img src="./assets/hardwares/ssd1106_128x64.jpg" width='150px'> | <img src="./assets/hardwares/ssd1106_64x32.jpg" width='150px'> | <img src="./assets/hardwares/st7302_122x250.jpg" width='150px'> | <img src="./assets/hardwares/nokia5110_84x48.jpg" width='150px'> |

### Display - Others

| LCD 16x2                                                 | LCD 20x4                                                 | tm1367 segment led                                      | mxa7219 led matrix                                                  | ws2812 led matrix                                                  | ws2812 led ring                                                  | ws2812 led strip                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- | ----------------------------------------------------------------- |
| <img src="./assets/hardwares/lcd1602.jpg" width='150px'> | <img src="./assets/hardwares/lcd2004.jpg" width='150px'> | <img src="./assets/hardwares/tm1367.jpg" width='150px'> | <img src="./assets/hardwares/mxa7219_led_matrix.jpg" width='150px'> | <img src="./assets/hardwares/ws2812_led_matrix.jpg" width='150px'> | <img src="./assets/hardwares/ws2812_led_ring.jpg" width='150px'> | <img src="./assets/hardwares/ws2812_led_strip.jpg" width='150px'> |

### Sensors - Temperature

| DHT11 Temp Humi                                        | DHT22 Temp Humi                                        | BMP280 Temp Humi Pressure                               | BMP180 Temp Humi Pressuree                              | sht3x High Accuracy Temp Humi                          | ds18b20 Temp                                             | MLX90614  Infrared Thermometer                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- | --------------------------------------------------------- |
| <img src="./assets/hardwares/dht11.png" width='150px'> | <img src="./assets/hardwares/dht22.jpg" width='150px'> | <img src="./assets/hardwares/bmp280.jpg" width='150px'> | <img src="./assets/hardwares/bmp180.jpg" width='150px'> | <img src="./assets/hardwares/sht3x.jpg" width='150px'> | <img src="./assets/hardwares/ds18b20.jpg" width='150px'> | <img src="./assets/hardwares/MLX90614.jpg" width='150px'> |

### Sensors - Distance&Acceleromter&Motion

| HC-SR04 Ultrasonic Distance                             | Vl53l0 ToF ranging                                      | Vl53l1 ToF ranging                                      | LIS3DH 3-Axis Motion                                    | MPU6050 6-Axis Motion                                    | MPU9250  9-Axis Motion                                   |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| <img src="./assets/hardwares/hcsr04.png" width='150px'> | <img src="./assets/hardwares/vl53l0.jpg" width='150px'> | <img src="./assets/hardwares/vl53l1.jpg" width='150px'> | <img src="./assets/hardwares/lis3dh.jpg" width='150px'> | <img src="./assets/hardwares/mpu6050.jpg" width='150px'> | <img src="./assets/hardwares/mpu9250.jpg" width='150px'> |

### Sensors - Others

| APDS9930 Light Proximity                                  | MAX30102 Oximeter Heart-Rate                              | TCS3472 Color                                            | HMC5883l 3-Axis  Compass                                  | QMC5883 3-Axis Magnetic                                  |
| --------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------- |
| <img src="./assets/hardwares/apds9930.jpg" width='150px'> | <img src="./assets/hardwares/max30102.jpg" width='150px'> | <img src="./assets/hardwares/tcs3472.jpg" width='150px'> | <img src="./assets/hardwares/hmc5883l.jpg" width='150px'> | <img src="./assets/hardwares/qmc5883.jpg" width='150px'> |

### Input - Button, Touch button, Joystick

| Button                                                    | Five buttons                                              | joystick model 1                                            | Joystick model 2                                            | Touch button 1                                         | Touch button 4                                         | IR Remote                                                  |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------- |
| <img src="./assets/hardwares/button_1.jpg" width='150px'> | <img src="./assets/hardwares/button_5.jpg" width='150px'> | <img src="./assets/hardwares/joystick_1.jpg" width='150px'> | <img src="./assets/hardwares/joystick_2.jpg" width='150px'> | <img src="./assets/hardwares/ttp_1.jpg" width='150px'> | <img src="./assets/hardwares/ttp_4.jpg" width='150px'> | <img src="./assets/hardwares/ir_remote.jpg" width='150px'> |


### Motor, Servo and Stepper

| L298N Motor Drive Controller                                 | L9110S Motor Drive Controller                                 | L9110S-4 Motor Drive Controller                                 | Stepper ULN2003 Driver                                           | SG90 Servo 180                                            | SG90 Servo 360                                            | MG90 Servo 180/360                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| <img src="./assets/hardwares/motor_l298n.jpg" width='150px'> | <img src="./assets/hardwares/motor_l9110s.jpg" width='150px'> | <img src="./assets/hardwares/motor_l9110s_4.jpg" width='150px'> | <img src="./assets/hardwares/stepper_uln2003.jpg" width='150px'> | <img src="./assets/hardwares/sg90-180.jpg" width='150px'> | <img src="./assets/hardwares/sg90-360.jpg" width='150px'> | <img src="./assets/hardwares/mg90-360.jpg" width='150px'> |

### RTC, DAC, RFID and Relay

| RTC DS3231                                              | RTC DS1307                                              | RTC DS1302                                              | DAC MCP4725                                              | RFID MFRC522                                             | Relay 1-channel                                                     | Relay 2-channel                                                     |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <img src="./assets/hardwares/ds3231.jpg" width='150px'> | <img src="./assets/hardwares/ds1307.jpg" width='150px'> | <img src="./assets/hardwares/ds1302.jpg" width='150px'> | <img src="./assets/hardwares/mcp4725.png" width='150px'> | <img src="./assets/hardwares/mfrc522.jpg" width='150px'> | <img src="./assets/hardwares/1-channel-5v-relay.jpg" width='150px'> | <img src="./assets/hardwares/2-Channel-5V-Relay.jpg" width='150px'> |


### Common Sensors

| IR detector                                                         | photorezistor                                                         | Optical barrier                                                         | microphone                                                  | RCWL-0516                                                                                          | PIR SB00422A-1                                                        | PIR HC-SR505                                                         |
| ------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------- |
| <img src="./assets/hardwares/IR_detector_sensor.jpg" width='150px'> | <img src="./assets/hardwares/photorezistor_module.jpg" width='150px'> | <img src="./assets/hardwares/Optical_barrier_module.jpg" width='150px'> | <img src="./assets/hardwares/microphone.jpg" width='150px'> | <img src="./assets/hardwares/Motion_detector_Microwave_Doppler_radar_RCWL-0516.jpg" width='150px'> | <img src="./assets/hardwares/PIR_modul_SB00422A-1.jpg" width='150px'> | <img src="./assets/hardwares/PIR_module_HC-SR505.jpg" width='150px'> |

| PIR 312                                                                   | Infrared flame                                                         | Hall probe                                                         | Current sensor                                                      | TCRT5000 IRtracing                                                                      | SW-1801P shock                                                                     | Light sensor                                                         |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| <img src="./assets/hardwares/PIR_modul_PIR_module_312.jpg" width='150px'> | <img src="./assets/hardwares/Infrared_flame_sensor.jpg" width='150px'> | <img src="./assets/hardwares/Hall_probe_module.jpg" width='150px'> | <img src="./assets/hardwares/30A_current_sensor.jpg" width='150px'> | <img src="./assets/hardwares/Module_with_TCRT5000_IR_tracing_sensor.jpg" width='150px'> | <img src="./assets/hardwares/Module_with_SW-1801P_shock_sensor.jpg" width='150px'> | <img src="./assets/hardwares/Light_sensor_module.jpg" width='150px'> |