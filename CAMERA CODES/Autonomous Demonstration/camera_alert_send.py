from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from imutils.video import VideoStream
import numpy as np
import imutils
import cv2
import time
#import Buzzer and flame sensor library
import RPi.GPIO as GPIO
# socket library 
from socket import *
#importing neopixel library
import board
import neopixel


GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  #numbering according to GPIO
pixels = neopixel.NeoPixel(board.D18, 16, brightness = 0.3)
GPIO.setup(22,GPIO.IN)  #FLAME SENSOR GPIO pin
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)  #BUZZER GPIO pin
pixels.fill((0, 0, 0))
time.sleep(1)

# create a socket and bind socket to the host
client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(('192.168.29.152',9009))
client_socket.connect(('172.20.10.4',9009))  #BOT Rpi IP address

print("\n\n\n\t\t*********  TURNING ON PYROBOT CAMERA SYSTEM  *************")
model = load_model('/home/pi/Desktop/FNF.h5')
vs = VideoStream(src=0).start()
time.sleep(2.0)
print("\n\n\n\t\t SYSTEM STARTED.... PRESS CTRL+C TO EXIT")

try:
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=300)
        image = cv2.resize(frame, (150, 150))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        (pred) = model.predict_classes(image) #CNN predicting fire
        a = pred[[0]]
        if(a==0):        
            if(GPIO.input(22)):
                text = 'KERAS: 1 --|-- SENSOR: 0'
                frame=cv2.putText(frame,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
                GPIO.output(17,1)#set buzzer OFF
                GPIO.output(27,0)
                pixels.fill((0, 255, 0))
            #both CNN and flame sensor detected fire
            else:
                text = 'KERAS: 1 --|-- SENSOR: 1'
                frame = cv2.putText(frame,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
                GPIO.output(17,0) #set buzzer ON
                GPIO.output(27,1)        
                time.sleep(0.3)
                GPIO.output(17,1) #set buzzer OFF
                GPIO.output(27,0)
                pixels.fill((255, 0, 0))
                client_socket.send('1'.encode()) #ROOM 1 ,2 AND 3 
        else:
            if (GPIO.input(22)==0):
                text = 'KERAS: 0 --|-- SENSOR: 1'
                frame=cv2.putText(frame,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
                GPIO.output(17,1)
                GPIO.output(27,0)     #set buzzer OFF
                pixels.fill((0, 255, 0))
            else:
                text = 'KERAS: 0 --|-- SENSOR: 0'
                frame=cv2.putText(frame,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
                GPIO.output(17,1) #set buzzer OFF
                GPIO.output(27,0)
                pixels.fill((0, 255, 0))
        cv2.imshow("Predicting Fire", frame)
        key = cv2.waitKey(60) & 0xFF
        if key == ord("q"):
            client_socket.close()
            break
except KeyboardInterrupt:
    print('\n\n\t\t Turning off pyrobot system abruptly.....on user command')
    cv2.destroyAllWindows()
    vs.stop()
    pixels.fill((0, 0, 0))
    GPIO.cleanup()
finally:
    print("turning off pyrobot system")
    cv2.destroyAllWindows()
    vs.stop()
    pixels.fill((0, 0, 0))
    GPIO.cleanup()
