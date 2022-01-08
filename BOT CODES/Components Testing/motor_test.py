import pyfirmata
import time
from pyfirmata import Arduino, util
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((250, 250))

board = pyfirmata.ArduinoMega("/dev/ttyACM0")

#rear right motor
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
    
print('\n\n\t\tDC MOTOR TEST FOR BOT\n')   
print('\nbooting up everything.......wait 2 sec')
time.sleep(2)
print('\n start to control the bot')
try:
    while True:        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key_input = pygame.key.get_pressed()                
                if key_input[pygame.K_UP]:                    
                    go_forward()
                elif key_input[pygame.K_RIGHT]:                   
                    go_right()
                elif key_input[pygame.K_LEFT]:                   
                    go_left()
                elif key_input[pygame.K_DOWN]:
                    go_backward()                    
                elif key_input[pygame.K_a]: 
                    go_diagonal_left()
                elif key_input[pygame.K_d]:  
                    go_diagonal_right()                    
                elif key_input[pygame.K_q]:
                    print("\nexit pygame and cleaning serial communication......")                    
                    pygame.quit()
                    board.exit()                    
                    break
            elif event.type == pygame.KEYUP:
                go_stop()
except KeyboardInterrupt:
    go_stop()        
    pygame.quit()
    board.exit()
    print('\ncleaning serial communication and exiting abruptly........!')
    time.sleep(2)
finally:
    go_stop()
    
   
        

