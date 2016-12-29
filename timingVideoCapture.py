import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
start_time = time.time()
file_name=str(int(start_time ))+'.avi'
print (file_name)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(file_name,fourcc, 10.0, (640,480))

print "Local current time :", start_time

while((time.time()-start_time)<10):
    if(cap.isOpened()):
	    ret, frame = cap.read()
	    if ret==True:
		frame = cv2.cvtColor(frame,0)
		out.write(frame)
		cv2.imshow('frame',frame)
	 	if cv2.waitKey(1) & 0xFF == ord('q'):
          	       break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
