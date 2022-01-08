import pyfirmata
import time
from pyfirmata import Arduino, util

'''DEFINING ARDUINO MEGA BOARD'''
board = pyfirmata.ArduinoMega("/dev/ttyACM0")

'''DEFINING DISTANCE SENSOR'''
sharpsensor_pin = board.get_pin('a:0:i')

'''DEFINING LINE FOLLOWER SENSOR'''
LF_1= board.get_pin('d:31:i')
LF_2 = board.get_pin('d:33:i')
LF_3 = board.get_pin('d:35:i')
LF_4 = board.get_pin('d:37:i')
LF_5 = board.get_pin('d:39:i')
LF_6= board.get_pin('d:41:i')
LF_7 = board.get_pin('d:43:i')

'''DEFINING MOTOR'''
#rear right
RR_motor_forward = board.get_pin('d:22:o')
RR_motor_backward = board.get_pin('d:24:o')
#front right motor
FR_motor_forward = board.get_pin('d:26:o')
FR_motor_backward = board.get_pin('d:28:o')
#rear left motor
RL_motor_forward = board.get_pin('d:34:o')
RL_motor_backward = board.get_pin('d:32:o')
#front left motor
FL_motor_forward = board.get_pin('d:38:o')
FL_motor_backward = board.get_pin('d:36:o')


def go_forward():
    FR_motor_forward.write(1)
    FR_motor_backward.write(0)
    RR_motor_forward.write(1)
    RR_motor_backward.write(0)
    FL_motor_forward.write(1)
    FL_motor_backward.write(0)
    RL_motor_forward.write(1)
    RL_motor_backward.write(0)
def go_backward():
    FR_motor_forward.write(0)
    FR_motor_backward.write(1)
    RR_motor_forward.write(0)
    RR_motor_backward.write(1)
    FL_motor_forward.write(0)
    FL_motor_backward.write(1)
    RL_motor_forward.write(0)
    RL_motor_backward.write(1)
def go_left():
    FR_motor_forward.write(1)
    FR_motor_backward.write(0)
    RR_motor_forward.write(1)
    RR_motor_backward.write(0)
    FL_motor_forward.write(0)
    FL_motor_backward.write(1)
    RL_motor_forward.write(0)
    RL_motor_backward.write(1)
def go_right():
    FL_motor_forward.write(1)
    FL_motor_backward.write(0)
    RL_motor_forward.write(1)
    RL_motor_backward.write(0)
    FR_motor_forward.write(0)
    FR_motor_backward.write(1)
    RR_motor_forward.write(0)
    RR_motor_backward.write(1)
def go_stop():
    FR_motor_forward.write(0)
    FR_motor_backward.write(0)
    RR_motor_forward.write(0)
    RR_motor_backward.write(0)
    FL_motor_forward.write(0)
    FL_motor_backward.write(0)
    RL_motor_forward.write(0)
    RL_motor_backward.write(0)
    
def go_diagonal_left():
    FL_motor_forward.write(1)
    FL_motor_backward.write(0)
    RL_motor_forward.write(0)
    RL_motor_backward.write(1)
    FR_motor_forward.write(0)
    FR_motor_backward.write(1)
    RR_motor_forward.write(1)
    RR_motor_backward.write(0)
def go_diagonal_right():
    FL_motor_forward.write(0)
    FL_motor_backward.write(1)
    RL_motor_forward.write(1)
    RL_motor_backward.write(0)
    FR_motor_forward.write(1)
    FR_motor_backward.write(0)
    RR_motor_forward.write(0)
    RR_motor_backward.write(1)
    
def go_forward_left():
    FL_motor_forward.write(1)
    FL_motor_backward.write(0)
    RR_motor_forward.write(1)
    RR_motor_backward.write(0)

def go_forward_right():
    FR_motor_forward.write(1)
    FR_motor_backward.write(0)
    RL_motor_forward.write(1)
    RL_motor_backward.write(0)

def go_backward_left():
    RL_motor_forward.write(0)
    RL_motor_backward.write(1)
    FR_motor_forward.write(0)
    FR_motor_backward.write(1)

def go_backward_right():
    FL_motor_forward.write(0)
    FL_motor_backward.write(1)
    RR_motor_forward.write(0)
    RR_motor_backward.write(1)

def avoid_obstacle():
    data=sharpsensor_pin.read()
    voltage = round((data*5),2)
    distance = int  (306.439 + voltage * (-512.611 + voltage * (382.268 + voltage * (-129.893 + voltage * 16.2537))) ) #for 150cm range sensor
    while distance<20:
            go_stop()
            print('bject')
            data=sharpsensor_pin.read()
            voltage = round((data*5),2)
            distance = int  (306.439 + voltage * (-512.611 + voltage * (382.268 + voltage * (-129.893 + voltage * 16.2537))) ) #for 150cm range sensor

def room_1_go():
    
    while True:              #BOT REACHED NODE 1
        avoid_obstacle()        
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True :
            print('\n\nBOT REACHED NODE 1')
            #go_stop()
            #ime.sleep(1)
            go_forward()
            time.sleep(0.5)
            break        
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True :              
            go_left()                       
        else:            
            go_forward()
            
            
    while True:                       # BOT REACHED NODE 2
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED NODE 2')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()
                if  LF_6.read() ==True:
                    break           
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()
        else:
            go_forward()
    
        
    while True:                      # BOT REACHED ROOM 1
        avoid_obstacle()
        
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED ROOM')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()
                if  LF_6.read() ==True:
                    go_stop()
                    break
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True:  
            go_left()       
        else:            
            go_forward()


def room_1_return():
    
    while True: #BOT REACHED NODE 2
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True :
            print('\n\nBOT REACHED NODE 2')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_right()
            time.sleep(1)
            while True:
                go_right()
                if   LF_3.read()==True :
                    break
            break
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:              
            go_left()                       
        else:            
            go_forward()
            
            
    while True: # BOT REACHED NODE 1
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED NODE 1')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(0.5)
            break
        elif LF_3.read()== True  and LF_6.read() == False :    
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True :  
            go_left()
        else:
            go_forward()
    
    while True: #BOT REACHED starting position
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED STARTING POSITION')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()               
                if  LF_6.read() ==True:
                    go_stop()
                    break 
            break
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()       
        else:
            go_forward() 
            
            

            
def room_3_go():
    
    while True:              #BOT REACHED NODE 1
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True :
            print('\n\nBOT REACHED NODE 1')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_right()
            time.sleep(1)
            while True:
                go_right()
                if   LF_3.read() ==True :
                    break
            break
                        
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
            
        elif LF_3.read()== False  and LF_6.read()== True :              
            go_left()                       
        else:            
            go_forward()
            
            
    while True:                       # BOT REACHED NODE 4
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED NODE 2')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_right()
            time.sleep(1)
            while True:
                go_right()
                if  LF_3.read() ==True:
                    break           
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()
        else:
            go_forward()
    
        
    while True:                      # BOT REACHED ROOM 3
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED ROOM')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()
                if  LF_6.read() ==True:
                    go_stop()
                    break
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True:  
            go_left()       
        else:            
            go_forward()
            


def room_3_return():
    while True:                       # BOT REACHED NODE 4
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED NODE 4')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()
                if  LF_6.read() ==True:
                    break           
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()
        else:
            go_forward()
    
    while True:                       # BOT REACHED NODE 1
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED NODE 2')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()
                if  LF_6.read() ==True:
                    break           
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()
        else:
            go_forward()
    
    while True: #BOT REACHED starting position
        avoid_obstacle()

        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED STARTING POSITION')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()               
                if  LF_6.read() ==True:
                    go_stop()
                    break 
            break
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()       
        else:
            go_forward() 
            
    
def room_2_go():
    while True:              #BOT REACHED NODE 1
        avoid_obstacle()
                                
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True :
            print('\n\nBOT REACHED NODE 1')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(0.5)
            break        
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True :              
            go_left()                       
        else:            
            go_forward()
            
            
    while True:                       # BOT REACHED NODE 2
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED NODE 2')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_right()
            time.sleep(1)
            while True:
                go_right()
                if  LF_3.read() ==True:
                    break           
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()
        else:
            go_forward()
    
    while True:              #BOT REACHED NODE 3
        avoid_obstacle()
                                
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True :
            print('\n\nBOT REACHED NODE 3')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(0.5)  
            break      
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True :              
            go_left()                       
        else:            
            go_forward()
    
    while True:                      # BOT REACHED ROOM 2
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED ROOM 2')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()
                if  LF_6.read() ==True:
                    go_stop()
                    break
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True:  
            go_left()       
        else:            
            go_forward()
            
def room_2_return():
    while True:              #BOT REACHED NODE 3
        avoid_obstacle()
                                
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True :
            print('\n\nBOT REACHED NODE 3')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(0.5) 
            break      
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True :              
            go_left()                       
        else:            
            go_forward()
    
    while True:                       # BOT REACHED NODE 2
        avoid_obstacle()
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED NODE 2')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()
                if  LF_6.read() ==True:
                    break           
            break
        elif  LF_3.read()== True  and LF_6.read() == False:    
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()
        else:
            go_forward()
    
    while True:              #BOT REACHED NODE 1
        avoid_obstacle()
                                
        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True :
            print('\n\nBOT REACHED NODE 1')
            #go_stop()
            #time.sleep(1)
            go_forward()
            time.sleep(0.5) 
            break      
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif LF_3.read()== False  and LF_6.read()== True :              
            go_left()                       
        else:            
            go_forward()
    
    while True: #BOT REACHED starting position
        avoid_obstacle()

        if LF_1.read()==True and LF_2.read()==True and LF_3.read() ==True and LF_4.read()==True  and LF_5.read() ==True  and LF_6.read() ==True and LF_7.read()==True:
            print('\n\nBOT REACHED STARTING POSITION')
            go_stop()
            time.sleep(1)
            go_forward()
            time.sleep(1.5)
            go_left()
            time.sleep(1)
            while True:
                go_left()               
                if  LF_6.read() ==True:
                    go_stop()
                    break 
            break
        elif LF_3.read()== True  and LF_6.read() == False:   
            go_right()
        elif  LF_3.read()== False  and LF_6.read()== True:  
            go_left()       
        else:
            go_forward() 
            

#Starting the iterator
it = util.Iterator(board)
it.start()
print('\n\n\t****  Starting the LINE FOLLOWER TEST wait for 6 seconds.  *****')
time.sleep(6) # let it start so that it doesn't print none
sharpsensor_pin.enable_reporting()
LF_1.enable_reporting()
LF_2.enable_reporting()
LF_3.enable_reporting()
LF_4.enable_reporting()
LF_5.enable_reporting()
LF_6.enable_reporting()
LF_7.enable_reporting()    
print('\n\t*****  Test started Press Ctrl+C to exit the test..  ***** \n')
    
try:
    while True:
        room_2_go()
        time.sleep(1)
        room_2_return()
        time.sleep(5)
except KeyboardInterrupt:
    print('\n\n\t\t Exiting the Test' )
    go_stop()    
    LF_1.disable_reporting()
    LF_2.disable_reporting()
    LF_3.disable_reporting()
    LF_4.disable_reporting()
    LF_5.disable_reporting()
    LF_6.disable_reporting() 
    LF_7.disable_reporting()
    sharpsensor_pin.disable_reporting()
    board.exit()
    time.sleep(2)
    
    
    
    








    
