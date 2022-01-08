import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.IN)
input = GPIO.input(15)
while True:
    print(GPIO.input(15))
    '''
    if (GPIO.input(15)):
        print("0")  #for no flame
    else:
        print("1")  # for flame
    '''
