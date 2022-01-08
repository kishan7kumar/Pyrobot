import pyfirmata
from pyfirmata import Arduino, util
import time

board = pyfirmata.ArduinoMega("/dev/ttyACM0") 
sharpsensor_pin = board.get_pin('a:0:i')

it = util.Iterator(board)
it.start()
print('\n\n\t****  Starting the DISTANCE SENSOR TEST wait for 6 seconds  *****')
time.sleep(6) # let it start so that it doesn''t print none
print('\n\t*****  Test started Press Ctrl+C to exit the test..  *****')
sharpsensor_pin.enable_reporting()
try:
    while True:     
        data=sharpsensor_pin.read()
        #adc=int(1023*data) #arduino conversion 1023 bits
        voltage = round((data*5),2)
        distance = int  (306.439 + voltage * (-512.611 + voltage * (382.268 + voltage * (-129.893 + voltage * 16.2537))) ) #for 150cm range sensor
        #distance = int ( 27.86 *((voltage)**-1.15) ) # for 80cm range sensor       
        if (distance>150):
            print('\t Voltage (in V)= ' , voltage , '\tDistance (in cm) = Out of Range')
        else:
            print ('\t Voltage (in V) = ', voltage, '\tDistance (in cm) = ', distance)  
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\n\n\t**********   exiting the test...   **********')
    time.sleep(1)
    sharpsensor_pin.disable_reporting()
    board.exit()

    
  
      
    
   
    
    
       

