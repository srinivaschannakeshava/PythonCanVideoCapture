import time

start_time = time.time()
print "Local current time :", start_time

while((time.time()-start_time)<10):
	pass

print("time difference : ",time.time()-start_time)

