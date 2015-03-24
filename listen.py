#!/usr/bin/env python
import network
import sys
import os
import time
import RPi.GPIO as GPIO

def buttonEventHandler(pin):
print "handling button event"
# give terminating command
time.sleep(1)
os.system("^C")
def main():
	# tell the GPIO module that we want to use the
	# chip's pin numbering scheme
	GPIO.setmode(GPIO.BCM)
	# Configuring PINS to be input/output
	# PIN2 is the vibration sensor
	GPIO.setup(2,GPIO.IN)
	# PIN3 is presence sensor
	GPIO.setup(3,GPIO.IN)
	# PIN4 is LED control
	GPIO.setup(4,GPIO.OUT)
	# PIN17 is Transister control 1
	GPIO.setup(17,GPIO.OUT)
	# PIN27 is Transister control 2
	GPIO.setup(27,GPIO.OUT)
	# PIN22, 10, 9 are pins without sensors attached.
	GPIO.setup(22,GPIO.OUT)
	GPIO.setup(10,GPIO.IN)
	GPIO.setup(9,GPIO.OUT)
	# Access card sensor PINS
	GPIO.setup(21,GPIO.OUT)
	GPIO.setup(20,GPIO.IN)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(7,GPIO.IN)
	GPIO.setup(8,GPIO.OUT)

    	def heard(phrase):
  	print "them:" + phrase

	print "Chat Program"

	#	 wait for  message 
	network.wait(whenHearCall=heard)

	while network.isConnected():
  		if phrase == 'open'
	      	# here we need to check the status of the door 
	      	output=os.system("/home/pi/checkstat.sh /home/pi/status closed 23")
	      	#TODO: need to verify that the return value is a string. 
	      	if output == 23
	          	# the door is closed, now we open it. 
	          	GPIO.output(4,True)
	          	# update the status of the door 
	          	os.system("echo open > /home/pi/status")
	        # otherwise do nothing, the door is already open. 
	    else if phrase == 'close'
	    	# check the status on the door for open
	    	output=os.system("/home/pi/checkstat.sh /home/pi/status open 23")
	      	#TODO: need to verify that the return value is a string. 
	      	if output == 23
	          	# the door is open, now we close it. 
	          	GPIO.output(4,False)
	          	# update the status of the door 
	          	os.system("echo closed > /home/pi/status")
	        # otherwise do nothing, the door is already open.

	GPIO.cleanup()
if __name__=="__main__":
main()


