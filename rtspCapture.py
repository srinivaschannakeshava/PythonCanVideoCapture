import numpy as np
import cv2

cap = cv2.VideoCapture("rtsp://192.168.0.12:554/")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
print("1 step",cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    print("2 step")
    if ret==True:
	print("3 step")
        frame = cv2.cvtColor(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
	print("breaking on ret")
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
