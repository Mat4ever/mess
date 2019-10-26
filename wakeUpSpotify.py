import os
import time

#TODO allowing more time formats like 6:00, 06:00, 6am, 6pm 
alarm_time = int(input("""On what time to go off?\nNumber of hours and minutes joined togheter.\nFor example 6am here is 60, 11:35am is 1135\n> """))
#TODO  add here formating, so 60 becomes 06:00
print("Okay. Going off at %s." % alarm_time)

while True:
	time_ = time.localtime()
	timeHM = str(time_[3]) + str(time_[4])
	if int(timeHM) == alarm_time:
		print("It's time")
		os.system("spotifycli --play")
		break
	print(timeHM)
	time.sleep(29)

