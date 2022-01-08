import pyfirmata
import time
from pyfirmata import Arduino, util

board = pyfirmata.ArduinoMega("/dev/ttyACM0")

LF_1= board.get_pin('d:31:i')
LF_2 = board.get_pin('d:33:i')
LF_3 = board.get_pin('d:35:i')
LF_4 = board.get_pin('d:37:i')
LF_5 = board.get_pin('d:39:i')
LF_6= board.get_pin('d:41:i')
LF_7 = board.get_pin('d:43:i')
it = util.Iterator(board)
it.start()
time.sleep(5) # let it start so that it doesn't print none
LF_1.enable_reporting()
LF_2.enable_reporting()
LF_3.enable_reporting()
LF_4.enable_reporting()
LF_5.enable_reporting()
LF_6.enable_reporting()
LF_7.enable_reporting()
try:
    while True:
        value1 = LF_1.read()
        print(value1)
except KeyboardInterrupt:
    board.exit()
    LF_1.disable_reporting()
    LF_2.disable_reporting()
    LF_3.disable_reporting()
    LF_4.disable_reporting()
    LF_5.disable_reporting()
    LF_6.disable_reporting()
    LF_7.disable_reporting()
    

   
