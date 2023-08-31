import io
import socket
import struct
from PIL import Image
import cv2
import numpy
import sys
import pandas as pd
import winsound
import threading
import pyfirmata
import time
from ultralytics import YOLO

model=YOLO('yolov8n.pt')


board = pyfirmata.Arduino('COM4')
led = board.get_pin('d:13:o')


#is_sound_playing = False
#def play_sound():
#    global is_sound_playing
#    if not is_sound_playing:
#        is_sound_playing = True
#        winsound.Beep(700, 2000)
#        is_sound_playing = False

   
led_on = False
def LED(light):
    global led_on
    if light == "on" and not led_on:
        led.write(1)
        led_on = True
    elif light == "off" and led_on:
        led.write(0)
        led_on = False


server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))  
server_socket.listen(0)
print("Listening")
connection = server_socket.accept()[0].makefile('rb')

try:
    pTime = 0
    img = None
    while True:
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        image_stream.seek(0)
        image = Image.open(image_stream)
        im = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
        
        results=model.predict(im)
    
        bbox_data = results[0].boxes.data
        bbox_info = pd.DataFrame(bbox_data).astype("float")
        
        LED("off")
        
        for index, row in bbox_info.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            conf = round(row[4], 2)
            object_index=int(row[5])
            object = results[0].names[object_index]
            if object == 'person':
                #sound_thread = threading.Thread(target=play_sound)
                #sound_thread.start()
                LED("on")
            
            object_text_size = cv2.getTextSize(str(object), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)[0]
            cv2.rectangle(im, (x1, y1), (x2, y2), (255, 255, 255), 2)
            cv2.putText(im, str(object), (x1, y1-2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(im, str(conf), (x1 + object_text_size[0] + 15, y1 - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(im, f"FPS: {str(int(fps))}", (0,15), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, cv2.LINE_AA)
        
        cv2.imshow('Video',im)
        if cv2.waitKey(1) & 0xFF == 27:
           break
    
    LED("off")
    cv2.destroyAllWindows()
    
finally:
    connection.close()
    server_socket.close()