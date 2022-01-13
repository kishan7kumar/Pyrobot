#This was the led ring that was used to display whether the fire was detected by camera system. It turned red(fire detected) and green (no fire)
import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 16,brightness = 0.3)

pixels.fill((0, 0, 0))
time.sleep(1)

'''green'''
pixels.fill((0, 255, 0))
time.sleep(2)

'''red'''
pixels.fill((255, 0, 0))
time.sleep(2)

'''blue'''
pixels.fill((0, 0, 255))
time.sleep(2)

'''white'''
pixels.fill((255, 255, 255))
time.sleep(2)
pixels.fill((0, 0, 0))
time.sleep(2)

