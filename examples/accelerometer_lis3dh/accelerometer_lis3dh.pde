import processing.serial.*;
import java.awt.event.KeyEvent;
import java.io.IOException;
Serial myPort;
String data="";
float roll, pitch,yaw;
void setup() {
  size (1200, 800, P3D);
  noStroke();
  myPort = new Serial(this, "COM7", 115200); // starts the serial communication
  myPort.bufferUntil('\n');
}
void draw() {
  background(233);
  translate(width/2, height/2, 100);
  textSize(22);
  text("Roll: " + int(roll) + "     Pitch: " + int(pitch), -100, 265);
  // Rotate the object
  rotateZ(radians(pitch));
  rotateX(radians(roll));
  textSize(30);  
  fill(0, 76, 153);
  box(386, 40, 200); // Draw box
  textSize(25);
  fill(255, 255, 255);
  text("MPY Blockly", -140, 10, 101);
}
// Read data from the Serial Port
void serialEvent (Serial myPort) { 
  // reads the data from the Serial Port up to the character '.' and puts it into the String variable "data".
  data = myPort.readStringUntil('\n');
  // if you got any bytes other than the linefeed:
  if (data != null) {
    data = trim(data);
    String items[] = split(data, ',');
    if (items.length > 1) {
            yaw = float(items[0]);
            pitch = float(items[1]);
            roll = float(items[2]);
    }
  }
}
