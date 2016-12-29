import cv2 as cv

vcap = cv.VideoCapture("rtsp://192.168.0.12:554/out.h264")

while(1):

    ret, frame = vcap.read()
    cv.imshow('frame', frame)
    cv.waitKey(1)
