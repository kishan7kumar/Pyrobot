
import time 
from imutils.video import VideoStream
from threading import Thread
import numpy as np
import cv2
import imutils


vs = VideoStream(usePiCamera=True).start()
time.sleep(1.0)

while True:
  
  frame = vs.read()
  frame = imutils.resize(frame, width=400)
  cv2.imshow("CAMERA TEST", frame)
  key = cv2.waitKey(60) & 0xFF
  if key == ord("q"):
    break
 
print("cleaning up...")
cv2.destroyAllWindows()
vs.stop()

