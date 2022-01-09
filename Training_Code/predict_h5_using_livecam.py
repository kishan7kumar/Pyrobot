from keras.models import load_model
from keras.preprocessing import image
#import matplotlib.pyplot as plt
from keras.preprocessing.image import img_to_array
from imutils.video import VideoStream
import numpy as np
import os
import imutils
import cv2
import time
   
print("[INFO] loading model...")
model = load_model('/home/pi/Desktop/testmodel1.h5')
vs = VideoStream(src=0).start()
time.sleep(2.0)
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=300)
	image = cv2.resize(frame, (150, 150))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	(pred) = model.predict_classes(image)
	a = pred[0]
	b = a[0]
	if(b==0):
		label = "fire"
		#output = imutils.resize(og, width=400)
		cv2.putText(frame, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2)
	else:
		label = "Not fire"
		#output = imutils.resize(og, width=300)
		cv2.putText(frame, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.9, (255, 0, 0), 3)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()   
    
