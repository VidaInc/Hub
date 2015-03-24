# A simple network chat program between to Raspberry Pi's

import network
import sys
import time

def heard(phrase):
  print "them:" + phrase

print "Chat Program"
# need to give the sending function an IP addreess
  network.call(127.0.1.1, whenHearCall=heard)

print "Chat away!"  
while network.isConnected():
	output=os.system("/home/pi/checkstat.sh /home/pi/status closed 23")
	      	#TODO: need to verify that the return value is a string. 
	      	if output == 23
	          	network.say('closed')
	        else if output == 1
	             network.say('open')
	time.sleep(1)