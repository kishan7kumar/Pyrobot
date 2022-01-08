import time
import RPi.GPIO as gpio
gpio.cleanup()
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)

try:
    while True:
        	gpio.output(11,1)
        	gpio.output(13,0)
        	
        	print("beep")
        	time.sleep(0.4)
        	gpio.output(11,0)
        	gpio.output(13,1) 
        	print("not beep")
       		time.sleep(0.4)
except KeyboardInterrupt:
            gpio.cleanup()
            exit
