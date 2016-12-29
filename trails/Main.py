import sftpOperations
import CanRead
import os
import cv2
import time
import thread
import paho.mqtt.publish as publish

#os.system('sudo rmmod uvcvideo')
#os.system('sudo modprobe uvcvideo nodrop=1 timeout=5000 quirk=0x80')

print("----------------------------------------------------")
os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ip link set can0 up')
print("CAN BUS UP")
print("----------------------------------------------------")
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fourcc = cv2.cv.CV_FOURCC(*'MJPG')
videoList=[];


def captureVideo():
#	print('capturing video')
	start_time = time.time()
	file_name=str(int(start_time ))+'.avi'
	out = cv2.VideoWriter(file_name,fourcc, 9 , (640,480))
	while((time.time()-start_time)<60):
	    if(cap.isOpened()):
		    ret, frame = cap.read()
		    if ret==True:
			out.write(frame)
			#cv2.imshow('frame',frame)
		 	if cv2.waitKey(1) & 0xFF == ord('q'):
		  	       break
	out.release()
	if(len(videoList)>=3):
		os.remove(videoList.pop(0));
	videoList.append(file_name);
	videoList.sort();
	return

thread.start_new_thread(CanRead.CanRead.statusSimulator,())
print("Capturing Video......")

while not CanRead.CanRead.getCanEventStatus() :
	captureVideo()
#        print "videoList : ",videoList
print("----------------------------------------------------")
print ('Event detected',videoList)
print("----------------------------------------------------")
print("Connecting to SFTP Server ...... ")
sftpOperations.sftpOperations.connectToSftp()
print ("SFPT Connection Established")
print("----------------------------------------------------")
print("pushing "+videoList[len(videoList)-1]+" to server")
print("----------------------------------------------------")
sftpOperations.sftpOperations.pushToServer(videoList[len(videoList)-1])
print("----------------------------------------------------")
print('closing SFTP connection....')
sftpOperations.sftpOperations.closeConnection()
print('SFTP connection closed')
print("----------------------------------------------------")
print('Sending Notification ....')
publish.single("com/bosch/incident/","{\"file\":\"/home/ubuntu/test/"+videoList[len(videoList)-1]+"\",\"lat\":\"12.936102\",\"lng\":\"77.612350\"}",hostname="test.mosquitto.org")
print('Notification sent')
print("----------------------------------------------------")




