# Code to test RPi temperature as it get heated up quickly because of deep learning model running on it
import os
import time
import cv2
def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))
while True:
	print(measure_temp())
	time.sleep(1)

# press Ctrl+C to exit	
 
