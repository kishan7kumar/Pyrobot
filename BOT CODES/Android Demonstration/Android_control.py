''' PYROBOT ANDROID CONTROL APPLICATION '''
import socket
import time
import pyfirmata
from pyfirmata import Arduino, util
board = pyfirmata.ArduinoMega("/dev/ttyACM0")
#voltagesensor1_pin = board.get_pin('a:4:i')   #pin 5 for 8.4V battery  and   pin4 for 12V battery
#voltagesensor2_pin = board.get_pin('a:5:i')   #pin 5 for 8.4V battery  and   pin4 for 12V battery

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

#battery gate
battery_gate_angle = board.get_pin('d:6:s')

#camera control
camera_yaxis_angle = board.get_pin('d:7:s')
camera_xaxis_angle = board.get_pin('d:8:s')

#nozzle control
nozzle_angle = board.get_pin('d:9:s')

#fan control
fan_A =  board.get_pin('d:10:o')
fan_B =  board.get_pin('d:11:o')

#extinguisher control
extinguisher_angle = board.get_pin('d:5:s')

def fan_on():
    fan_A.write(0)
    fan_B.write(1)
def fan_off():
    fan_A.write(0)
    fan_B.write(0)
    
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

# resetting everything to default positon
camera_xaxis_angle.write(95)  #x axis center postion
battery_gate_angle.write(79)   #battery gate close
camera_yaxis_angle.write(90)  #y axis center postion
nozzle_angle.write(20)
extinguisher_angle.write(9)

class BotAndroidControl(object):
    def __init__(self, host, port):
        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.streaming()
        
    def streaming(self):
        print('\n Test started... Press Ctrl+C anytime to exit testing\n\n')
        while True:
            print('waiting for user command')
            self.connection, self.client_address = self.server_socket.accept()
            go_stop()
            try:
                while True:
                    app_command = self.connection.recv(1024).decode() #1024 is buffer size 
                    #BOT CONTROL
                    if (app_command == '1'):
                        print('forward')
                        go_forward()
                    elif (app_command == '2'):
                        print('back')
                        go_backward()
                    elif (app_command == '3'):
                        print('stop')
                        go_stop()
                    elif (app_command == '4'):
                        print('rotate left')
                        go_left()
                    elif (app_command == '5'):
                        print('rotate right')
                        go_right()
                    elif (app_command == '15'):
                        print('digaonal left')
                        go_diagonal_left()                        
                    elif (app_command == '14'):
                        print('diagonal right')
                        go_diagonal_right()
                    
                    #CAMERA CONTROL
                    elif (app_command == '6'):
                        print('camup')
                        camera_yaxis_angle.write(40) 
                    elif (app_command == '7'):
                        print('camdown')
                        camera_yaxis_angle.write(120)
                        
                    elif (app_command == '9'):
                        print('camleft')
                        camera_xaxis_angle.write(25)
                        
                    elif (app_command == '8'):
                        print('camright')
                        camera_xaxis_angle.write(180)
                    elif (app_command == '12'):
                        print('x axis center')
                        camera_xaxis_angle.write(95)
                        
                    elif (app_command == '13'):
                        print('y axis center')
                        camera_yaxis_angle.write(90)
                        
                    #FIRE CONTROL
                    elif (app_command == '10'):
                        print('FAN on')
                        fan_on()
                        #extinguisher_angle.write(90)
                    elif (app_command == '11'):
                        print('FAN off')
                        fan_off()
                        #extinguisher_angle.write(9)
                    elif (app_command == '19'):
                        print('nozzle up')
                        nozzle_angle.write(80)
                    elif (app_command == '18'):
                        print('nozzle down')
                        nozzle_angle.write(20)
                    #BATTERY GATE CONTROL    
                    elif (app_command == '16'):
                        print('gate open')
                        battery_gate_angle.write(9)                                                 
                    elif (app_command == '17'):
                        print('gate close')
                        battery_gate_angle.write(79)
                    else:
                        break
            except KeyboardInterrupt:
                self.connection.close()
                self.server_socket.close()
                break
if __name__ == '__main__':  
    h, p = "172.20.10.8", 9002  # IP ADDRESS of BOT Raspberry Pi
    print('\n\t\t*********** PYROBOT ANDROID CONTROL TEST ****************')
    print('\n\tPress any button on Android Application to start the test.......')
    #it = util.Iterator(board)
    #it.start()
    #voltagesensor1_pin.enable_reporting()
    #voltagesensor2_pin.enable_reporting()
    try:
        BotAndroidControl(h, p)
    except KeyboardInterrupt: 
        print('\n\n\t\tClosing  the testing program.......... wait for 2 sec')
        camera_xaxis_angle.write(95)  #x axis center postion
        battery_gate_angle.write(79)   #battery gate close
        camera_yaxis_angle.write(90)  #y axis center postion
        nozzle_angle.write(90)
        extinguisher_angle.write(9)
        #voltagesensor1_pin.disable_reporting()
        #voltagesensor2_pin.disable_reporting()
        go_stop()
        time.sleep(2)
        board.exit()
