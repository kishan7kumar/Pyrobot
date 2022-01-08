import pyfirmata
from pyfirmata import Arduino, util
import time


board = pyfirmata.ArduinoMega("/dev/ttyACM0") 
voltagesensor1_pin = board.get_pin('a:4:i')   #pin 5 for 8.4V battery  and   pin4 for 12V battery
voltagesensor2_pin = board.get_pin('a:5:i')   #pin 5 for 8.4V battery  and   pin4 for 12V battery

#starting the iterator
it = util.Iterator(board)
it.start()
print('\n\n\t****  Starting the VOLTAGE SENSOR TEST wait for 6 seconds.  *****')
time.sleep(6) # let it start so that it doesn''t print none
print('\n\t*****  Test started Press Ctrl+C to exit the test..  ***** \n')
voltagesensor1_pin.enable_reporting()
voltagesensor2_pin.enable_reporting()
try:
    while True:     
        data1=voltagesensor1_pin.read() #pyfirmata conversion 0-1 float values
        data2=voltagesensor2_pin.read() 
        #adc=int(1023*data) #arduino conversion 0 - 1023 bits
        Vout1= round(( data1*5),2) #voltage in volts coming from analog pin
        Vout2= round(( data2*5),2)
        Vin1= Vout1 / (7500/37500) # voltage sensor reading
        Vin2= Vout2  / (7500/37500) # voltage sensor reading
        final_vtg1 = round( (Vin1), 1) 
        final_vtg2 = round( (Vin2+0.35), 1) 
        print('\t\t\tVoltage1 = ',final_vtg1,' V','\tVoltage2 = ',final_vtg2,' V') # rounding off to two decimal
        time.sleep(1)
except KeyboardInterrupt:
    
    print('\n\n\t\t**********   exiting the test...   **********')
    time.sleep(1)
    voltagesensor1_pin.disable_reporting()
    voltagesensor2_pin.disable_reporting()
    board.exit()
