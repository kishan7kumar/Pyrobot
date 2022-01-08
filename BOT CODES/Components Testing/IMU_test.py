import FaBo9Axis_MPU9250
import time
import sys
import pyfirmata
from pyfirmata import Arduino, util

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
board = pyfirmata.ArduinoMega("/dev/ttyACM0") 
buzzer_A =  board.get_pin('d:45:o')
print('\n\n\t\tPreparing to start the test..... please wait 5 seconds')
time.sleep(5)
print('\n\t\t Test is start press CTRL +C to exit anytime \n')

try:
    while True:
        '''
        accel = mpu9250.readAccel()
        print ("\nax = " , ( accel['x'] ) )
        print ("\nax = " , ( accel['x'] ) )
        print ( " ay = " , ( accel['y'] ) )
        print (" az = " , ( accel['z'] ) )
        '''
        
        gyro = mpu9250.readGyro()
        print ("\ngx = " , ( int(gyro['x']) )   )
        print ("gy = " , ( int(gyro['y']) )   )
        print ("gz = " , ( int(gyro['z'] ))   )
        if  int(gyro['y'])  >2 or int(gyro['y'])  <-1 or  int(gyro['z'] ) >2 :
            print('\n\t\tATTENTION BOT IS BEEN MISHANDELD !!!!!!!!!!!!!!!!!!!!')
            buzzer_A.write(1)
            time.sleep(0.2)
            buzzer_A.write(0)
         
        
            
        
        '''
        mag = mpu9250.readMagnet()
        print ( " \nmx = " , (int( mag['x'] ) ) )
        print ("my = " , ( int(mag['y'] ) ))
        print ("mz = " , ( int(mag['z'] )))
        if int( mag['x'] ) <=-1:
            print('BOT FACING BACK')
        elif  int(mag['y'] ) >=65:
            print('BOT FACING LEFT')
        elif int(mag['y'] ) <=5:
            print('BOT FACING RIGHT')
        elif int( mag['x'] ) >=39 and int( mag['x'] )<45 :
            print('BOT FACING FRONT')
        '''
        
        
        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
