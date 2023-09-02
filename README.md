# Smart Surveillance System Using Raspberry Pi and Arduino

A smart surveillance system that uses the Raspberry Pi camera for live video streaming. The video is sent over the network to the PC, where object detection is then performed. If a certain object is detected, in this case 'person', then a signal is sent to the Arduino, which then lights up the LED for the duration of the object's presence within the video feed.


## Project Overview
The project consists of three main components:

1. Raspberry Pi: The Raspberry Pi captures live video and sends it to the PC over the network.
2. PC: The PC receives the video feed, performs object detection using YOLO (You Only Look Once), and displays the video with object overlays. When a 'person' is detected, it signals the Arduino to turn on an LED.
3. Arduino: The Arduino controls an LED, which lights up when a 'person' is detected.

## Prerequisites
Before you start, make sure you have the following hardware and software installed:
### Hardware Components
1. Raspberry Pi 4B
2. camera module
3. PC (Windows or Linux)
4. Arduino Uno R3 board
5. LED (red)
6. A resistor (220Ω)
7. Two jumper wires
8. Breadboard
### Software Dependencies
- Python 3.7.3 on both the Raspberry Pi and PC
- Raspberry Pi: picamera, socket, struct, time, io
- PC: socket, struct, PIL, cv2, numpy, sys, pandas, winsound, threading, pyfirmata, ultralytics YOLO

## Setup
1. Install the required dependencies on both platforms
2. Connect the Raspberry Pi camera module to your Raspberry Pi.
3. Make sure that your Raspberry Pi has a network connection (Wi-Fi or Ethernet).
4. Place the "client.py" code from the "Raspberry Pi Codes" folder into the Raspberry Pi.
5. Place the "server.py" code onto your PC.
6. Connect the Arduino board to your PC.
7. Place the LED, resistor, jumper wires and the breadboard in accordance to the setup below: ![image](https://github.com/j16m3n4m6y4l/Smart-Surveillance-System-Using-Raspberry-Pi-and-Arduino/assets/132979609/5ab4da69-cfb6-463d-a395-787800257889)

9. In 'server.py', Modify the Arduino's COM port (e.g., 'COM4') to match the one on your PC, as indicated in the Device Manager.
10. In 'client.py', replace '111.111.1.111' with your PC's IP

## Usage
Run 'server.py' in your PC:
```
python server.py
```

Then run 'client.py' in your Raspberry Pi:
```
python client.py
```
If successful, a window of the video feed from the Raspberry Pi should pop up on your PC. The LED should light up whenever a particular object is detected.

## Demonstration


https://github.com/j16m3n4m6y4l/Smart-Surveillance-System-Using-Raspberry-Pi-and-Arduino/assets/132979609/0f5db49e-6f36-48f4-87ea-d81bf5c4c49c


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements
- This project uses the Ultralytics YOLO model for object detection. Make sure to follow their licensing and usage terms.
- Inspiration and ideas for this project came from various online tutorials and communities. Thank you to the Raspberry Pi, Arduino, and computer vision communities for their valuable resources.

  - [Live Video Stream](https://github.com/Arijit1080/Live-Video-Stream-from-Raspberry-Pi-Camera-over-the-Network)
  - [Object Detection](https://github.com/freedomwebtech/yolov8-opencv-win11)
  - [LED Controller](https://github.com/Chando0185/led_controller_python_arduino)
