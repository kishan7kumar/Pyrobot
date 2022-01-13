# This code will allow to take pictures from camera system to make dataset for training the CNN
import pygame
from pygame.locals import *
from picamera import PiCamera
from time import sleep
from imutils.video import VideoStream
import imutils
import time
import cv2


vs = VideoStream(src=0).start()
pic = 1
print("\n\n\t\tStart Collecting Dataset...... Press C for clicking picture")
print("\n\n\t\tPress Q to stop taking pictures")
while True:
    
    frame = vs.read()
    frame = cv2.resize(frame, (640 , 480))
    frame1 = cv2.resize(frame, (150 , 150))
    cv2.imshow('frame',frame1)
    
    key = cv2.waitKey(60)
    if key == ord("c"):
        picture = "/home/pi/fire_dataset/image_%d.jpg"%pic
        cv2.imwrite(picture, frame)
        print('Image_ '+str(pic))
        pic=pic+1       
    if key ==ord("q"):
        break
        
