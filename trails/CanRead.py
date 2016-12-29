import time
import can 
 
class CanRead:
  
  eventStatus=False
  can_interface='can0'
 
  @staticmethod
  def getCanEventStatus():
	return CanRead.eventStatus

  @staticmethod
  def setCanEventStatus(status):
	CanRead.eventStatus=status

  @staticmethod
  def statusSimulator():
#	startTime=time.time()
#	while((time.time()-startTime)<240):
	bus = can.interface.Bus(CanRead.can_interface,bustype='socketcan')
	while True :
		message=bus.recv()
		if message is not None:
			if message.arbitration_id == 640 :
				CanRead.eventStatus=True
				print("----------------------------------------------")
				print("Crash event detected ")
				print("----------------------------------------------")
				print("CanRead.eventStatus ",CanRead.eventStatus)
				break	
   	return
