import pyfirmata
import time
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((250, 250))

board = pyfirmata.ArduinoMega("/dev/ttyACM0")  #,baudrate=57600) #,baudrate=9600,timeout=None)
battery_gate_angle = board.get_pin('d:6:s')
camera_yaxis_angle = board.get_pin('d:7:s')
camera_xaxis_angle = board.get_pin('d:8:s')
camera_xaxis_angle.write(95)  #x axis center postion
battery_gate_angle.write(78)  #battery gate close
camera_yaxis_angle.write(90)  #y axis center postion


#input_pin1=board.servo_config(6,min_pulse=544,max_pulse=2400,angle=0)
print('\n\n\t\t\tBooting up the system.........wait')
time.sleep(1)
print('\n\t\tstart')
try:
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key_input = pygame.key.get_pressed()
                
                if key_input[pygame.K_q]:                    
                    pygame.quit()
                    board.exit()
                    break
                
                elif key_input[pygame.K_UP]:
                    #battery_gate_angle.write(78)
                    camera_yaxis_angle.write(40)
                
                elif key_input[pygame.K_LEFT]:                    
                    camera_xaxis_angle.write(25)
                
                elif key_input[pygame.K_RIGHT]:                    
                    camera_xaxis_angle.write(180)

                elif key_input[pygame.K_DOWN]:
                    #battery_gate_angle.write(9)
                    camera_yaxis_angle.write(120)
                                        
                

except KeyboardInterrupt:
    print('closing connection abruptly on USER COMMAND...........')
    pygame.quit()
    board.exit()
    
    
finally:
    print('closing connection properly.......')
    pygame.quit()
    
